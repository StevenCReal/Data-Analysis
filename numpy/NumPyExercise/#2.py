import numpy as np

z1 = np.zeros((8, 8), int)
z1[1::2, ::2] = 1  # 分两种情况解决，奇数行和偶数行
z1[0::2, 1::2] = 1
print(z1)

z2 = np.random.random((10, 10))
zmin, zmax = z2.min(), z2.max()  # 寻找最小值，最大值
print(z2)
print(zmin)
print(zmax)

z3 = np.tile(np.array([[0, 1], [1, 0]]), (4, 4))        # 利用tile()构造棋盘，reps参数指定堆叠次数
print(z3)
