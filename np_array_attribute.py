import numpy as np
'''
a = np.array([[1,2,3],[3,4,5],[4,5,6]])

print(a.shape)     #tuple consisting of array dimensions
print(a.ndim)      #number of array dimension
print(a.itemsize)  #length of each element of array in bytes
'''

x = np.empty([3,2], dtype=int)
print(x)