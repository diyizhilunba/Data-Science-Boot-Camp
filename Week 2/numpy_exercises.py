# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 19:47:28 2024

@author: mayil
Define two custom numpy arrays, say A and B. Generate two new numpy arrays by 
stacking A and B vertically and horizontally.
"""

import numpy as np

arr1 = np.array([1,2,3,4])
arr2 = np.array([4,5,6,7])

print("-------------------------------")
#stack them together
arr3 = np.vstack((arr1, arr2))
arr4 = np.hstack((arr1, arr2))

print("-------------------------------")
#test
print(arr3)
print(arr4)


print("-------------------------------")
#find the intersection
arr5 = np.intersect1d(arr1, arr2)
print(arr5)

print("-------------------------------")
#extract all numbers in A which are in a specific range
range_mask = np.where((arr1 >= 1) & (arr1 <= 3))
arr6 = arr1[range_mask]
print(arr6)

print("-------------------------------")
#Filter the rows of iris_2d that has petallength (3rd column) > 1.5
# and sepallength (1st column) < 5.0
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

#print(iris_2d)

filtered_rows = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)]