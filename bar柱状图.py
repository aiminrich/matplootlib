import matplotlib.pyplot as plt
import numpy as np

n = 12    #规定有12个柱状图（12个向上的和12个向下的）
X = np.arange(n)   #产生从0-11的数字
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)  #从uniform distrubution中产生从0.5-1的数值
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

plt.bar(X, +Y1)
plt.bar(X,-Y2)

plt.xlim(-.5,n)
plt.ylim(-1.25,1.25)
plt.xticks(())
plt.yticks(())
plt.show()