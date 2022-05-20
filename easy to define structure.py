import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True,sharey=True)   #将figure分成2行2列，共享x轴和y轴
ax11.scatter([1,2],[1,2])
plt.show()