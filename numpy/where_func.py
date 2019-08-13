import numpy as np

arr = np.random.randn(4, 4)
print(arr)
result = np.where(arr > 0, 2, arr)
print(result)
