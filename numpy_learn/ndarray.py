import numpy as np

# Generate some random data
data = np.random.randn(2, 3)
print(data)
data = data * 10
print(data)
data = data + data
print(data)
# Every array has a shape, a tuple indicating the size of each dimension, 
    # and a dtype, an object describing the data type of the array
print(data.shape)
print(data.dtype)

# Creating ndarrays
# list can store different types of data by storing pointers
mylist = [1, 2, 'Hi', 3.2, "Crazy"]
print(mylist)
# numpy offers N-dimensional array for numeric computation, 
    # which makes it easy to generate array-oriented computation
mylist2 = [2, 4, 6, 8, 10]
array = np.array(mylist2)
print(array * 2)

array2 = np.zeros(5)
array3 = np.ones(5)
array4 = np.arange(15)
print(array2)
print(array3)
print(array4)

# type conversion
arr1 = np.array([1,3,5,7], dtype=np.float32)
print(arr1)
# Calling astype always creates a new array (a copy of the data),
    # even if the new dtype is the same as the old dtype.
arr1.astype(np.int32)
print(arr1.dtype)
