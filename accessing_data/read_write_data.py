import pandas as pd
"""read a file with header row"""
df = pd.read_csv('D:\pydata-book\examples\ex1.csv')
print(df)
df2 = pd.read_table('D:\pydata-book\examples\ex1.csv', sep=',')  #sep分隔符
print(df2)
"""read a file without header row"""
# accept the default row pandas assigns to you
df3 = pd.read_csv('D:\pydata-book\examples\ex2.csv', header=None)
# or specify names yourself
df4 = pd.read_csv(
    'D:\pydata-book\examples\ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
