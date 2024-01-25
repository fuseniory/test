import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')


# R@1 on Charade-STA
y1 = [46.45, 47.03, 47.90]
# y2 = [80.25, 80.65, 80.92, 81.19, 81.61]
# y3 = [87.26, 87.52, 87.95, 88.22, 88.62]

fig, ax = plt.subplots(figsize=(5.4, 7.2), dpi=100)
# ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
# 设置自变量的范围和个数
# x = ["Base", "+Attention", "+Scene", "+MultiMap", "+MultiSig"]
x = ["Global", "Boundary", "Multi-Scale"]
# 画图
# ax.plot(x, y1, label='IoU=0.7', linestyle='-', marker='*', markersize='10', color='blue')
ax.plot(x, y1, label='R1@IoU=0.5',linestyle='-', marker='*', markersize='10', color='blue')
# ax.plot(x, y2, label='IoU=0.5', linestyle='-', marker='p', markersize='10', color='red')
# ax.plot(x, y3, label='IoU=0.3', linestyle='-', marker='o', markersize='10', color='limegreen')
# 设置坐标轴
ax.set_xlabel('Modules', fontsize=15)
ax.set_ylabel('Performance', fontsize=15)
# 设置刻度
ax.tick_params(axis='both', labelsize=13)
# 显示网格
# ax.xaxis.grid(True, linestyle='-')
ax.yaxis.grid(True, linestyle='-')
# 添加图例
legend = ax.legend(loc='best')

plt.show()
fig.savefig('./a1.pdf', format='pdf')












