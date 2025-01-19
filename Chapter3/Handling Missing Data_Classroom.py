
"""Nguyễn Tấn Phúc
    N21DCDK022  """
    
"""
Trong 3 file IT Salary Survey, sẽ có những cột dữ liệu là rỗng (null) hoặc Not A Number
Bài tập này dùng để đếmm tổng cộng field có giá trị null và giá trị NA, sau đó print ra màn hình.
"""

import pandas as pd

#Open 3 files IT Eu from 2018 - 2019
df_2018 = pd.read_csv("D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Chapter3/IT_Salary_Survey_EU_2018.csv")
df_2019 = pd.read_csv("D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Chapter3/IT_Salary_Survey_EU_2019.csv")
df_2020 = pd.read_csv("D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Chapter3/IT_Salary_Survey_EU_2020.csv")

# Check for missing values in each column for 2018, 2019, and 2020 datasets
missing_2018 = df_2018.isnull().sum()
missing_2019 = df_2019.isnull().sum()
missing_2020 = df_2020.isnull().sum()

print(missing_2018)
print(missing_2019)
print(missing_2020)
