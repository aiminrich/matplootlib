import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)     #为了好看

plt.scatter(X,Y,s = 75,c = T,alpha=0.5)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.xticks(())   #括号中带有一个什么都没有的括号，就是隐藏ticks
plt.yticks(())
plt.show()