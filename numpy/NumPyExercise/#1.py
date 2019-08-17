import numpy as np

print(np.__version__)  # 查看numpy的版本
np.__config__.show()  # 查看numpy的配置

z = np.zeros((2, 3))
print(z)

z[1, 2] = 1
print(z)

array1 = np.arange(0, 10)
print(array1)

array2 = np.arange(9).reshape(3, 3)  # reshape()
print(array2)

nz1 = np.nonzero(array1)
nz2 = np.nonzero(
    array2)  # nonzero() returns a tuple of arrays, one for each dimension of a
print(nz1)
print(nz2)

unitVector = np.eye(3)  # eye() 生成单位向量矩阵
print(unitVector)

diagVector1 = np.diag(
    array1)  # diag() ，如果传入的是一维数组，返回以一维数组为对角线的二维数组；传入的是二维数组，则返回对角线的一维数组
diagVector2 = np.diag(array2)
diagVector3 = np.diag(array1, k=1)
print(diagVector1)
print(diagVector2)
print(diagVector3)

rand1 = np.random.random((3, 3))  # 这个random模块属于numpy模块，与单独的random模块不同
rand2 = np.random.randint(1, 10, (3, 3))
rand3 = np.random.randn(3, 3)  # 随机数符合标准正态分布
print(rand1)
print(rand2)
print(rand3)
