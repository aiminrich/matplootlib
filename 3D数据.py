import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
#X,Y value
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)   #把X,Ymesh到底面上
R = np.sqrt(X**2 + Y**2)
#高
Z = np.sin(R)
ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))   #rstride表示线的跨度，越小，线越密；cstride表示颜色的跨度，越小，颜色越多
ax.contourf(X,Y,Z,zdir='x',offset=-2,cmap = 'rainbow')
ax.set_zlim(-2,2)

plt.show()
