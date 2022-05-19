#如何在matplotlib中打印图像
import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.313660827978,0.365348418405,0.423733120134,
                      0.375348418405,0.439599930621,0.525083754405,
                      0.423733120134,0.525083754405,0.61536351379]).reshape(3,3)

plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')  #origin = upper时，输出的像素值和输入的对应；=lower时，相反
plt.colorbar(shrink = 0.9)
plt.xticks(())
plt.yticks(())
plt.show()