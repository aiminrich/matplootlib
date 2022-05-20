import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()
gs = gridspec.GridSpec(3,3)   #将整个figure分成3行3列
ax1 = plt.subplot(gs[0,:])        #ax1在figure中占了第0行，把所有的列都占了
ax2 = plt.subplot(gs[1,:2])     #ax2在figure中占了第1行，从0列到的第一列
ax3 = plt.subplot(gs[1:,2])     #ax3在figure中占了第1，2行，第二列
ax4 = plt.subplot(gs[-1,0])    #ax4在figure中占第2行，第1列
ax5 = plt.subplot(gs[-1,-2])   #ax5在figure中占了第2行，第1列
plt.show()
