import pandas as pd
import numpy as np

ser1 = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(ser1.rank(method='min'))
