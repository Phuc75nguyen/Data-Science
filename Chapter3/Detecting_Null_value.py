import pandas as pd

# Đọc file CSV
df = pd.read_csv("D:\COMPUTER SCIENCE PTITHCM\PYTHON4AI\Data Science\IT Salary Survey EU  2020.csv")
# Kiểm tra toàn bộ DataFrame để xem có giá trị null không
null_data = df.isnull()
print("Các giá trị null trong DataFrame:\n", null_data)
#đếm số lượng các giá trị là null trong data frame:

