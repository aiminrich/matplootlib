import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1=2*x+1
y2 = x**2

plt.figure()
plt.plot(x,y1,color = 'green',linewidth = 2.0,linestyle = '--')
plt.plot(x,y2,color = 'red',linewidth = 2.0,linestyle = '-')
plt.xlim(-1,3)
plt.ylim(-3,3)
plt.xlabel('I am x')
plt.ylabel('I am y')
new_ticks = np.linspace(-1,3,6)  #换坐标轴的单位方式，从[-1，3]之间分成6个数
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-3,-1,1,3],
           ['really bad','bad','good','perfect'])
plt.show()

