import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation   #从主模块里生成次模块

fig,ax = plt.subplots()
x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))
def animate(i):
    line.set_ydata(np.sin(x+i/10))
    return line,
def init_func():
    line.set_ydata(np.sin(x))
    return line,
ani = animation.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init_func,interval=20,blit=False)
plt.show()