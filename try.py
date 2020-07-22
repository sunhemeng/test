import csv
from matplotlib import pyplot as plt

episodes = 100
error_avg = []
# 读取CSV文件数据
filename = 'FadingChannel_OutdatedCSI_Error_DDPG_S3_rho0.9_SNR10.0_PS320_lr5e-05_df0.0_W4_sigOU0.8_thetaOU0.5_Critic_V2.csv'
with open(filename) as f:  # 打开这个文件，并将结果文件对象存储在f中
    reader = csv.reader(f)  # 创建一个阅读器reader
    header_row = next(reader)  # 文件中的下一行 跳过第一行

    for row in reader:
        error_avg.append(row[0])
        print(error_avg)

error_avg_float = []
for num in error_avg:
    error_avg_float.append(float(num))
print(error_avg_float)

plt.figure(0)
plt.plot(error_avg_float, '-g.', markersize=1)
plt.axis([0, episodes, 0, 1.1])
plt.xlabel('Episode')
plt.ylabel('Error')
plt.title('Error')
plt.yscale('symlog', nonposy='clip', linthreshy=10**-8)
plt.grid()
plt.show()
# # 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red', alpha=0.5)  # 实参alpha指定颜色的透明度，0表示完全透明，1（默认值）完全不透明
# plt.plot(dates, lows, c='blue', alpha=0.5)
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # 给图表区域填充颜色
# plt.title('Daily high and low temperature-2004', fontsize=24)
# plt.xlabel('', fontsize=16)
# plt.ylabel('Temperature(F)', fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
# fig.autofmt_xdate()  # 绘制斜的日期标签
# plt.show()







