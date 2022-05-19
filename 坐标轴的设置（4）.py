import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = x*2+1
y2 = x**2

plt.figure()
plt.plot(x,y1,color = 'green',linewidth = 2.0,linestyle = '--')
plt.plot(x,y2,color = 'pink',linewidth = 2.0,linestyle = '-')
plt.xlim(-2,2)
plt.ylim(-3,3)
plt.xlabel('I am x')
plt.ylabel('I am y')
new_ticks = np.linspace(-2,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-3,-1,0,1,3],
           ['really bad','bad','ok','good','perfect'])
#gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('None')
ax.spines['top'].set_color('None')
ax.xaxis.set_ticks_position('bottom')   #用下面的坐标轴来代替x轴
ax.yaxis.set_ticks_position('left')        #用左边的坐标轴来代替y轴
#挪动坐标轴
ax.spines['bottom'].set_position(('data',0))  #x轴的原点绑定在y轴的0处 ，还有不同的参数：outward,axes(定位在百分之多少的位置)
ax.spines['left'].set_position(('data',0))       #y轴的原点绑定在x轴的0处
plt.show()