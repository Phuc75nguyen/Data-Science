import pandas as pd

# Đọc file CSV
df = pd.read_csv("D:\COMPUTER SCIENCE PTITHCM\PYTHON4AI\Data Science\IT Salary Survey EU  2020.csv")


# Xóa khoảng trắng ở đầu/cuối tên cột
df.columns = df.columns.str.strip()

# Tạo MultiIndex từ các cột 'City' và 'Position'
df_multiindex = df.set_index(['City', 'Position'])

# In kết quả để kiểm tra
print(df_multiindex.head())
