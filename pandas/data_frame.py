import pandas as pd
import numpy as np

data = {
    'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
    'year': [2000, 2001, 2002, 2001, 2002, 2003],
    'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]
}
frame = pd.DataFrame(data)
print(frame)

frame2 = pd.DataFrame(
    data,
    columns=['year', 'state', 'pop', 'debt'],
    index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)
print(frame2.columns)
print(frame2.year)
print(frame2['state'])

#return a row
print(frame2.loc['three'])

#modify dataframe
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2['debt'])

#Assign a column that doesn't exist
frame2['eastern'] = frame2.state == 'Ohio'
print(frame2['eastern'])

#delete a column
del frame2['eastern']
print(frame2.columns)

# a nested dict of dicts
pop = {
    'Nevada': {
        2001: 2.4,
        2002: 2.9
    },
    'Ohio': {
        2000: 1.5,
        2001: 2.3,
        2002: 3.1
    }
}
frame3 = pd.DataFrame(pop)
print(frame3)
print(frame3.T)

# frame[直接输入，默认访问的是column]，
# 而frame.drop(直接输入，默认访问的是row,或者说是axis=0)

# loc 和iloc是用来访问row的
print('\n')
print(frame3.iloc[1, 1])
print('\n')
print(frame3.iat[1, 1])

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
print(df1+df2)
print(df1.add(df2, fill_value=0))
