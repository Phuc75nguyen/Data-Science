import pandas as pd

# Đọc dữ liệu từ file CSV
df_2018 = pd.read_csv("D:\COMPUTER SCIENCE PTITHCM\PYTHON4AI\Data Science\IT Salary Survey EU  2018.csv")
df_2019 = pd.read_csv("D:\COMPUTER SCIENCE PTITHCM\PYTHON4AI\Data Science\IT Salary Survey EU  2020.csv")

# Đổi tên các cột của df_2019 để khớp với df_2018
df_2019.rename(columns={
    'Zeitstempel': 'Timestamp',
    'Seniority level': 'Your level',
    'Position (without seniority)': 'Position',
    'Years of experience': 'Years of experience',
    'Yearly brutto salary (without bonus and stocks)': 'Current Salary',
    'Yearly brutto salary (without bonus and stocks) one year ago. Only answer if staying in same country': 'Salary one year ago',
    'Main language at work': 'Main language at work',
    'Company size': 'Company size',
    'Company type': 'Company type'
}, inplace=True)

# Chọn các cột giống nhau
common_columns = [
    'Timestamp', 'Age', 'Gender', 'City', 'Position', 'Years of experience', 'Your level',
    'Current Salary', 'Salary one year ago', 'Main language at work', 'Company size', 'Company type'
]

# Chọn các cột có trong cả hai DataFrame
df_2018_selected = df_2018[common_columns]
df_2019_selected = df_2019[common_columns]

# Nối hai DataFrame
df_combined = pd.concat([df_2018_selected, df_2019_selected], ignore_index=True)

# In kết quả
print(df_combined)
