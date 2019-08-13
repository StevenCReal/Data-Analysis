import numpy as np

points = np.arange(-5, 5, 0.01)  # 1000 equally spaced points

xs, ys = np.meshgrid(points, points)
print(ys)

z = np.sqrt(xs**2 + ys**2)
print(z)