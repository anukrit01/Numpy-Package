import numpy as np
'''
#Reading and Writing from text files
arr = np.loadtxt('file.txt')
print(arr)
np.savetxt('newfile.txt', arr)
'''

#Reading and Writing from CSV files
arr = np.genfromtxt('my_file.csv', delimiter=',')
print(arr)
np.savetxt('newfile.csv', arr, delimiter=',')