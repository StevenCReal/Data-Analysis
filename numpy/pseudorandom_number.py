import numpy as np 
import random

samples = np.random.normal(size =(4,4))
print(samples)

position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)