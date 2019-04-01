import numpy as np

arr = np.random.randn(3,6)
print(arr)
arr.sort(0) #passing axis 0 
print(arr)

"""get sorted unique values in an array"""
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names)) #return a copy
print(sorted(set(names))) # corresponding with Line 10
