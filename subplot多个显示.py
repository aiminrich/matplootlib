#如何在一张figure中展示多个函数
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(2,2,1)  #将整个figure分成两行两列，在第一个位置plot一个东西
plt.plot([0,1],[0,1])
plt.subplot(2,2,2)
plt.plot([0,1],[0,2])
plt.subplot(2,2,3)
plt.plot([0,1],[0,3])
plt.subplot(2,2,4)
plt.plot([0,1],[0,4])
plt.show()