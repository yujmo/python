import matplotlib.pyplot as plt

# 代码中的“...”代表省略的其他参数
ax = plt.subplot(111)

# 设置刻度字体大小
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

# 设置坐标标签字体大小
ax.set_xlabel(..., fontsize=20)
ax.set_ylabel(..., fontsize=20)

# 设置图例字体大小
ax.legend(..., fontsize=20)
