import pandas as pd


df1 = pd.DataFrame([[6, 3, 7], [6, 9, 2]], index=["00","01"],columns=['A', 'B', 'C'])

print(df1)


# hai phép toán bên dưới giống kết quả với nhau
print(df1 - df1.iloc[0])

print(df1.subtract(df1.loc['00']))