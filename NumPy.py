# import numpy
# arr = numpy.array([1,2,3,4,5])
# print(arr)
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(arr)
# import numpy as np
# print(np.__version__)
# import numpy as np
# arr = np.array([1,2,3,4,5]) # 1d array
# print(arr)
# print(type(arr))
# import numpy as np 
# arr = np.array(42)# 0D array
# print(arr)
# import numpy as np
# arr = np.array([[1,2,3],[4,5,6]]) # 3d Array
# print(arr)
# import numpy as np
# arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(arr)
# import numpy as np
# a = np.array(42)
# b = np.array([1,2,3,4,5])
# c = np.array([[1,2,3],[4,5,6]])
# d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)
# import numpy as np 
# arr = np.array([1,2,3,4,5], ndmin=5)
# print(arr)
# print("Number of dimensions: ",arr.ndim)
# import numpy as np
# arr = np.array([1,2,3,4])
# print(arr[0])
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
# import numpy as np
# arr = np.array([1,2,3,4], dtype='c')
# print(arr)
# print(arr.dtype)
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )
# import numpy as np
# arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print("Second element of the first row: ",arr[0,1])
# print("Fifth element of the second row:",arr[1,4])
# import numpy as np
# arr = np.array([1,2,3,4,5])
# x = arr.copy()
# arr[0] = 42
# print(arr)
# print(x)
# import numpy as np
# arr = np.array([1,2,3,4,5])
# x = arr.view()
# arr[0] = 42
# print(arr)
# print(x)
# import numpy as np
# arr = np.array([1,2,3,4,5])
# x = arr.view()
# x[0] = 20
# print(arr)
# print(x)
# import numpy as np
# arr = np.array([1,2,3,4,5])
# x = arr.copy()
# y = arr.view()
# arr[0] = 42
# print(x.base)
# print(y.base)
# import numpy as np
# arr = np.array([1,2,3,4],ndmin=5)
# print(arr.shape)
# import numpy as np
# arr = np.array([1,3,6,2,5])
# print(np.sort(arr))
# arr = np.array(["Banana","Apple","Cherry"])
# print(np.sort(arr))
# arr = np.array([True,False,True])
# print(np.sort(arr))
# import numpy as np
# arr = np.array([[3,2,4],[5,0,1]])
# print(np.sort(arr))
# import numpy as np 
# arr = np.array([1,2,3,4,5,4,4])
# x = np.where(arr == 4)
# print(x)
# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8])
# x = np.where(arr%2 == 0)
# print(x)
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
x = np.where(arr%2 == 1)
print(x)