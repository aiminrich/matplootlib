import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)     #从[-1,1]之间等距离选择50个点

y = x**2
plt.plot(x,y)                       #显示坐标图像，x代表横坐标，y代表纵坐标
plt.show()                         #显示整幅图像