import numpy as np

arr1 = np.array([[2., 3., 4.], [1.1, 1.2, 1.3]])
print(arr1 > 2)

# the data is not copied, and any modifications to the view will be reflected in the source array.
arr2 = np.arange(10)
print(arr2)
arr_slice = arr2[5:8]
print(arr_slice)
arr2[5:8] = 6
print(arr_slice)
arr_slice[:] = 233
print(arr2)