import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0,1,n)  #生成1024均值为0，方差为1的随机数
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)  #for color value为了好看

plt.scatter(X,Y,s= 75,c=T,alpha=0.5)  #绘制散点图，大小为75，颜色由T函数生成，透明度为50%
plt.xlim((-1.5,1.5))
plt.ylim(-1.5,1.5)
plt.show()