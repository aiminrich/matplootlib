import matplotlib.pyplot as plt
import  numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure()
plt.plot(x,y1,color = 'black',linewidth = 2.0,linestyle = '--')
plt.plot(x,y2,color = 'yellow',linewidth = 2.0,linestyle = '-')
plt.xlim(-1,3)          #设置x轴的范围
plt.ylim(-2,2)         #设置y轴的范围
plt.xlabel('I am x')     #描述x轴和y轴
plt.ylabel('I am y')
plt.show()

