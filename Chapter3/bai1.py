import pandas as pd

df = pd.read_csv("D:\COMPUTER SCIENCE PTITHCM\PYTHON4AI\Data Science\IT Salary Survey EU  2020.csv")

print(df.describe())

#tìm hiểu phần esstntial xem mấy cái hàm nó sắp xếp như thế nào

print (df.City)

print (df.iloc[:5, :6])