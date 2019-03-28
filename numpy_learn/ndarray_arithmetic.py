import numpy as np

arr1 = np.array([[2., 3., 4.], [1.1, 1.2, 1.3]])
print(arr1 > 2)

"""array slicing, view and copy"""
# **the data is not copied, and any modifications to the view will be reflected in the source array.
arr2 = np.arange(10)
print(arr2)
arr_slice = arr2[5:8]
print(arr_slice)
arr2[5:8] = 6
print(arr_slice)
arr_slice[:] = 233
print(arr2)
# If you want a copy of a slice of an ndarray instead of a view:
arr_copy = arr2[5:8].copy()

# two dimensional array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d[1])
print(arr2d[0][1])
print(arr2d[0, 1])

# two dimensional arrays slice
arr2d_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d_2[:2])
print(arr2d_2[:, :2])
# attention! these 2 are different.
print(arr2d_2[:, 1])
print(arr2d_2[:, :1])

"""Boolean Indexing"""
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print(names)
print(data)

#The boolean array must be of the same length
# as the array axis it’s indexing.
cond = names=='Bob'
print(data[cond])
print(data[~cond])
cond = (names=='Bob')|(names=='Will')   # brackets are necessary
print(data[cond])

"""other array computation"""
data2 = np.random.rand(4,5)
print(data2)
print(data2[data2<0.5])

data3 =np.empty((4,6),dtype='int')
for i in range(4):
    data3[i]=i
print(data3)
print(data3[[2,0,1],:2])
print(data3[[-1],[1,2]])
