import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = x*2+1
y2 = x**2

plt.figure()
l1, = plt.plot(x,y1,color = 'green',linewidth = 2.0,linestyle = '--',label = 'y1')
l2,= plt.plot(x,y2,color = 'pink',linewidth = 2.0,linestyle = '-',label = 'y2')
#打legend图
plt.legend(handles =[l1,l2,],labels =['y1','y2'],loc ='best')   #handles是传线的，
plt.xlim(-2,2)
plt.ylim(-3,3)
plt.xlabel('I am x')
plt.ylabel('I am y')
new_ticks = np.linspace(-2,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-3,-1,0,1,3],
           ['really bad','bad','ok','good','perfect'])

plt.show()