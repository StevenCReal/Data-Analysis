import numpy as np
x = np.array([[2,3,4],[5,6,7]])
y= np.array([[-3,1],[5,3],[3,2]])

result1 = x.dot(y)
print(result1)
result2 = np.dot(x,y)
print(result2)

result3 = np.dot(x, np.ones(3))
print(result3)

from numpy.linalg import inv,qr
X = np.random.randn(5,5)
mat = X.T.dot(X)
print(mat)
inv_mat = inv(mat)
print(inv_mat)
result = mat.dot(inv_mat)
print(result)

q,r =qr(mat)
print(r)