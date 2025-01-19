import pandas as pd
import numpy as np

"""df = pd.DataFrame([[6,3,7,4], [6,9,2,6],[7,4,3,7]], columns=['A', 'B', 'C', 'D'])
print(df)
print(np.sum(df/ 4))
"""


df1 = pd.DataFrame([[6, 3, 7], [6, 9, 2]], columns=['A', 'B', 'C'])
df2 = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['A', 'B'])

print(df1)
print(df2)


print(df1 + df2)


print(df1.add(df2, fill_value =0))

