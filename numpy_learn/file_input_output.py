import numpy as np
arr1 = np.arange(10)
arr2 = np.arange(5)

np.save('some_array',arr1)
arr_load1 = np.load('some_array.npy')
print(arr_load1)

np.savez('array_archive.npz',a=arr1,b=arr2)
arr_load2 = np.load('array_archive.npz')
print(arr_load2['b'])