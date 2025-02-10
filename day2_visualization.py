# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np  # 添加 numpy 库

# 1. 读取清洗后的数据
data = pd.read_csv("cleaned_data_utf8.csv", encoding='gb2312')

# 2. 设置绘图风格
sns.set_style("whitegrid")  # 白色网格背景
plt.rcParams["font.sans-serif"] = ["SimHei"]  # 设置中文字体
plt.rcParams["axes.unicode_minus"] = False  # 解决负号显示问题

# 3. 创建画布
fig, ax = plt.subplots(figsize=(10, 6))

# 4. 绘制散点图（颜色映射回火时间）
scatter = ax.scatter(
    x=data["Quenching_Temp(℃)"],
    y=data["硬度（HV）"],
    c=data["Tempering_Time(h)"],
    cmap="cool",  # 蓝绿色渐变
    s=150,  # 增大点的大小
    marker="s",  # 方形标记
    edgecolor="yellow"  # 黄色边缘
)

# 5. 添加线性趋势线
z = np.polyfit(data["Quenching_Temp(℃)"], data["硬度（HV）"], 1)
p = np.poly1d(z)
plt.plot(data["Quenching_Temp(℃)"], p(data["Quenching_Temp(℃)"]), "r--", label="趋势线")

# 6. 添加标注
ax.set_xlabel("淬火温度 (℃)", fontsize=12, labelpad=10)
ax.set_ylabel("硬度 (HV)", fontsize=12, labelpad=10)
ax.set_title("淬火温度与硬度关系（颜色表示回火时间）", fontsize=14, pad=20)

# 7. 添加颜色条
cbar = plt.colorbar(scatter)
cbar.set_label("回火时间 (h)", fontsize=12)

# 8. 添加图例
plt.legend(fontsize=12)

# 9. 保存图片
plt.savefig("temp_hardness_plot.png", dpi=300, bbox_inches="tight")
plt.show()