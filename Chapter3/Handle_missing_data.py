import pandas as pd
import numpy as np

df = pd.DataFrame([[1, np.nan, 2], [2,
3, 5], [np.nan, 4, 6]])


print(df.dropna())

print(df.dropna(axis='columns',
how='all'))

print(df.dropna(axis='rows',
thresh=3))