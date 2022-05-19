import matplotlib.pyplot as plt
import numpy as np

n = 12    #规定有12个柱状图（12个向上的和12个向下的）
X = np.arange(n)   #产生从0-11的数字
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)  #从uniform distrubution中产生从0.5-1的数值
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

plt.bar(X, +Y1,facecolor = '#9999ff',edgecolor = 'white')
plt.bar(X,-Y2,facecolor = '#ff9999',edgecolor = 'white')

for x,y in zip(X,Y1):    #同时把x和y都传进去X和Y1中
    #ha: horizontal alignment对齐方式
    plt.text(x,y+0.05,'%.2f'% y,ha = 'center',va = 'bottom')                 #第一个参数是x的位置，第二个参数是y的位置,第三个参数是的对齐方式，第四个参数是纵向对齐方式
for x,y in zip(X,Y2):    #同时把x和y都传进去X和Y1中
    #ha: horizontal alignment对齐方式
    plt.text(x,-y-0.05,'-%.2f'% y,ha = 'center',va = 'top')

plt.xlim(-.5,n)
plt.ylim(-1.25,1.25)
plt.xticks(())
plt.yticks(())
plt.show()