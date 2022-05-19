import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1= 2*x+1
y2= x**2

plt.figure()
plt.plot(x,y1)


plt.figure(num=4,figsize=(8,5))
plt.plot(x,y2)

plt.show()