# -*- coding: utf-8 -*-
import pandas as pd

# 文件的绝对路径
file_path = r"C:\Users\wang\OneDrive\桌面\Day1\data.xlsx"

# 读取数据
try:
    data = pd.read_excel(file_path)
    print("数据读取成功！前5行数据：\n", data.head())
except Exception as e:
    print("错误！请检查：")
    print(f"1. 文件是否在当前目录\n2. 文件名是否正确\n3. 错误详情: {e}")

# 数据清洗
if not data.empty:
    clean_data = data.dropna()
    print("\n清洗后数据量：", len(clean_data))

    # 保存结果
    clean_data.to_csv(r"C:\Users\wang\OneDrive\桌面\Day1\cleaned_data.csv", index=False)
    print("已生成 cleaned_data.csv")
else:
    print("无有效数据可处理")