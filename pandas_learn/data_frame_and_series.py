import pandas as pd 
import numpy as np 

frame1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=list('abcd'))
ser1 = frame1.iloc[0]
ser2 = frame1['a']
frame1.sub(ser2, axis='index')

