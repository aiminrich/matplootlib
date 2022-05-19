import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return(1-x/2 + x**5 + y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)
#把颜色放到等高线上
plt.contourf(X,Y,f(X,Y),8,alpha = 0.75,cmap = plt.cm.hot)   #8代表有几种颜色，等高线的高度分了10 部分
#画等高线的线
C = plt.contour(X,Y,f(X,Y),8,colors = 'black',linewidth =0.5)
#加数字描述
plt.clabel(C,inline = True,fontsize = 10)
plt.xticks(())
plt.yticks(())
plt.show()