# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])
# plt.plot(xpoints, ypoints)
# plt.show()
# print(matplotlib.__version__)#to know the version of matplotlib
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
# xpoints = np.array([1, 8])
# ypoints = np.array([3, 10])
# plt.plot(xpoints, ypoints)
# plt.show()
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([5,8,1,10])
plt.plot(ypoints, marker = '*')
plt.show()
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# x = np.array([6, 2, 7, 11])
# y = np.array([3, 8, 1, 10])
# font1 = {'family':'serif', 'color': 'blue', 'size':20}
# font2 = {'family':'serif', 'color': 'darkred', 'size':15}
# plt.plot(x)
# plt.plot(y)
# plt.title("Massmatic students score card", fontdict= font1, loc='left')#loc for alignment
# plt.xlabel("total marks", fontdict= font2)
# plt.ylabel("total score", fontdict= font2)
# plt.grid(axis='y', color = 'green', linestyle = '--', linewidth = 0.5)
# plt.show()
# plot 1
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)
#plot 2
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()