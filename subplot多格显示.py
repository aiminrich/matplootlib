import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#nethod1：subplot2grid
import numpy as np

plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)   #第一个括号是将整个figure分成3行3列，第二个括号是ax1的起始位置，colspan为ax1所占的列，rowspan为ax1所占的行
ax1.plot([1,2],[1,2])
ax1.set_title('ax1_title')
ax2 = plt.subplot2grid((3,3),(1,0),colspan=1,rowspan=2)
ax2.plot([2,3],[2,3])
ax2.set_title('ax2 title')
ax3 = plt.subplot2grid((3,3),(1,1),colspan=2,rowspan=1)
ax3.plot([3,4],[3,4])
ax3.set_title('ax3 title')
ax4 = plt.subplot2grid((3,3),(2,1),colspan=2,rowspan=1)
ax4.scatter(np.arange(5),np.arange(5))
ax4.set_title('ax4 title')
ax4.set_xlim(1,4)
ax4.set_ylim(1,4)
plt.show()