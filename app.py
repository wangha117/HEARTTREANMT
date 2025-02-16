import sys
import joblib
import pandas as pd
from flask import Flask, render_template, request

# 打印 Python 可执行文件路径和 sys.path
print("Python executable:", sys.executable)
print("sys.path:", sys.path)

app = Flask(__name__)

# 加载优化后的模型
try:
    model = joblib.load('model/optimized_model.pkl')
    print("模型加载成功，文件未损坏。")
except Exception as e:
    print(f"模型加载失败，文件可能已损坏。错误信息：{e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 获取表单数据
    c_percent = float(request.form['c_percent'])
    quench_temp = float(request.form['quench_temp'])
    temper_time = float(request.form['temper_time'])
    
    # 计算额外的特征
    temp_interaction = quench_temp * temper_time  # 淬火温度和回火时间的交互项
    c_temp_ratio = c_percent / quench_temp  # 碳含量与淬火温度的比值
    
    # 转换为模型输入格式
    input_data = pd.DataFrame(
        [[c_percent, quench_temp, temper_time, temp_interaction, c_temp_ratio]],
        columns=['C％', 'Quenching_Temp(℃)', 'Tempering_Time(h)', 'Temp_Interaction', 'C_Temp_Ratio']
    )
    
    # 预测
    prediction = model.predict(input_data)[0]
    return f"预测硬度值：{prediction:.1f} HV"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)