# f = open("demo.txt", "r")
# print(f.read())
# f = open("E:\\demo1.txt", "r")
# print(f.read())
# f = open("E:\\demo1.txt", "r")
# print(f.read(5))
# f = open("E:\\demo1.txt", "r")
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f = open("E:\\demo1.txt", "r")
# for x in f:
#     print(x)
# f = open("E:\\demo1.txt", "r")
# print(f.readline())
# f.close()
# f = open("E:\\demo1.txt", "a")
# f.write("massmatic is under the ageis of akhil bhartiya cyber suraksha sangathan")
# f.close()
# f = open("E:\\demo1.txt", "r")
# print(f.read())
# f = open("E:\\demo1.txt", "w")# w method are overwrite the file
# f.write("massmatic is under the ageis of akhil bhartiya cyber suraksha sangathan")
# f.close()
# f = open("E:\\demo1.txt", "r")
# print(f.read())
# f = open("E:\\demo2.txt", "x")
# f.write("we are creating a new file")
# f.close()
# f = open("E:\\demo2.txt", "r")
# print(f.read())
# import os
# os.remove("demo.txt")
# import os
# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
# else:
#     print("this file does not exists")
# import os
# os.rmdir("python")
# import numpy
# arr = numpy.array([1,2,3,4,5])
# print(arr)
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)
# import numpy as np
# print(np.__version__)
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))
# import numpy as np
# arr = np.array(42)# 0d array
# print(arr)
# import numpy as np
# arr = np.array([[1,2,3],[4,5,6]])#2d array
# print(arr)
# import numpy as np
# arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]) #3d array
# print(arr)
# import numpy as np
# a = np.array(42)
# b = np.array([1,2,3,4,5])
# c = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# d = np.array([[1,2,3],[4,5,6]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)
# import numpy as np
# arr = np.array([1,2,3,4], ndmin=5)
# print(arr)
# print('number of dimensions:', arr.ndim)
# import numpy as np
# arr = np.array([1,2,3,4])
# print(arr[2])
# import numpy as np
# arr = np.array([1,2,3,4])
# print(arr[2] + arr[3])
# import numpy as np
# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print('second element of first row:', arr[1,4])
# import numpy as np
# arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print('third element of the second row', arr[0,1,2])
# import numpy as np
# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print('last element for the second dimension:', arr[1,-1])
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7])
# print(arr[1:5])
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7])
# print(arr[:4])
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7])
# print(arr[-3:-1])
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7])
# print(arr[1:5:2])
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7])
# print(arr[::2])
#2d array slicing
# import numpy as np
# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr[1,1:4])
# import numpy as np
# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr[0:2,2])
# import numpy as np
# arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
# print(arr[1:2,1:4])
# import numpy as np
# arr = np.array([1,2,3,4])
# print(arr.dtype)
# import numpy as np# display unicode string
# arr = np.array(['apple', 'banana', 'cherry'])
# print(arr.dtype)
# import numpy as np
# arr = np.array(['pineapplecherry'])
# print(arr.dtype)
# import numpy as np
# arr = np.array([1,2,3,4], dtype='S4')
# print(arr)
# print(arr.dtype)

# import numpy as np
# arr = np.array([1,2,3,4], dtype='f')
# print(arr)
# print(arr.dtype)
# import numpy as np
# arr = np.array([1,2,3,4], dtype='i4')
# print(arr)
# print(arr.dtype)
# import numpy as np
# arr = np.array([1,2,3,4], dtype='m')
# print(arr)
# print(arr.dtype)
import numpy as np
arr = np.array([1,2,3,4], dtype='c')
print(arr)
print(arr.dtype)
"""i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )"""