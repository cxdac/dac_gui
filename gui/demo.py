import serial
import datetime
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import threading

# 初始化数据
max_length = 24 * 60  # 数据缓冲区的最大长度，这里假设为一天中的分钟数
t = np.linspace(0, max_length - 1, max_length)  # 时间轴
y = np.zeros(max_length)  # 初始化值数组

# 设置图表
plt.figure(figsize=(10, 6))
plt.xlim(0, max_length)  # 设置x轴范围
plt.ylim(0, 200)  # 设置y轴范围
line, = plt.plot(t, y, '-o')

# 配置Arduino串口
arduinoserial = serial.Serial('COM3', 9600)

# 定义读取Arduino数据的函数
def read_arduino_data():
    if arduinoserial.is_open:
        try:
            data = arduinoserial.readline().decode().strip()  # 读取一行数据并解码
            light_intensity = float(data)  # 将字符串转换为浮点数
            return light_intensity
        except Exception as e:
            print("Arduino读取错误：", e)
            return None

# 更新函数
def update(frame):
    # 从Arduino读取数据
    light_intensity = read_arduino_data()
    if light_intensity is not None:
        y[frame % max_length] = light_intensity  # 更新数据
        line.set_data(t, y)
    return line,

# 创建动画
ani = FuncAnimation(plt.gcf(), update, frames=np.arange(0, max_length), blit=True, interval=100)

# 检查并执行每日重置
def check_and_reset():
    while True:
        now = datetime.datetime.now()
        if now.hour == 0 and now.minute == 0:
            y[:] = 0  # 将所有数据点重置为0
            plt.cla()  # 清除当前轴
            plt.xlim(0, max_length)  # 重新设置x轴范围
            plt.ylim(0, 100)  # 重新设置y轴范围
            line, = plt.plot(t, y, '-o')  # 重新绘制线条
        time.sleep(60)  # 每分钟检查一次时间

# 启动检查和重置
thread = threading.Thread(target=check_and_reset)
thread.daemon = True
thread.start()

plt.show()
