import numpy as np

x= np.random.randn(8)*5
y= np.random.randn(8)*5
print(x)
print(y)

arr1 = np.maximum(x,y)
print(arr1)

arr_fraction, arr_integer = np.modf(x)
print(arr_fraction)
print(arr_integer)