import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y = x*2+1

plt.figure(num=1,figsize=(8,5))
plt.plot(x,y,linewidth = 2.0,linestyle = '-',label = y)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

x0 = 1
y0 = 2*x0+1
plt.scatter(x0,y0,s = 50,color = 'b')#scatter是plt一个点
plt.plot([x0,x0],[y0,0],'k--',lw = 2.5)   #k代表黑色
plt.show()