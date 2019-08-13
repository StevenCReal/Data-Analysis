import numpy as np
import pandas as pd 

obj1 = pd.Series([4,7,-5,3])
print(obj1)
print(obj1.values)
print(obj1.index)

obj2 = pd.Series([4,7,-5,3],index =['b','c','a','d'])
print(obj2)
print(obj2['a'])

print(obj2[obj2>0])
print(np.exp(obj2))

"""Create a Series by passing a dict"""
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3) # Attention: the indices are sorted!
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj3 = pd.Series(sdata, index = states) # 并非按顺序排列，而是会进行下标匹配，看结果即明白
print(obj3)
print(pd.isnull(obj3))
print(pd.notnull(obj3))
print(obj3.isnull())

