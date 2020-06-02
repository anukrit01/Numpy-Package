
#Creating a Single - Dimensional NumPy Array
import numpy as np 
a = np.array([1,2,3])
print(a)

'''
#Creating a Multi - Dimensional NumPy Array
ar = np.array([[1,2,3],[7,8,9],[4,5,6]])
print(ar)


#'arange' method for single dimensional
arr = np.arange(10,100)
print(arr)


#'zeros' method
b = np.zeros((3,5))
print(b)


#Creating array from existing data
x = [1,2,3]
y = np.asarray(x)
print(y)


#Restructuring a numpy array
c = np.zeros(8)
c3d = c.reshape((2,2,2))
print(c3d)


#Slicing
arr = np.arange(20)
arr_slice = slice(1,10,2)
print(arr[arr_slice])


arr = np.arange(20)
print(arr[1:5])
'''

#Extracting specific rows and columns using slicing
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print (a)
print(a[0:2,0:2])