"""
EX4 Draw box plot  for Age data of dataset IT salary.
"""

import pandas as pd
import matplotlib.pyplot as plt


# đọc dữ liệu
df_2018 = pd.read_csv("D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Data Visualization/IT_Salary_Survey_EU_2018.csv")
df_2019 = pd.read_csv("D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Data Visualization/IT_Salary_Survey_EU_2019.csv")
df_2020 = pd.read_csv("D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Data Visualization/IT_Salary_Survey_EU_2020.csv")

#Nối 3 dữ liệu IT trên thành 1, dùng hàm concat() do pandas hỗ trợ
df_combined = pd.concat([df_2018, df_2019, df_2020], ignore_index=True)

#Chọn field Age để vẽ biểu đồ box plot
age_data = df_combined['Age']
# print ra màn hình để kiểm tra age_data
#print(age_data)

#Có các giá trị bị NaN hoặc Null, phải xử lí loại bỏ
age_data_clean = age_data.dropna()

#Vẽ Box plot cho Age

plt.figure(figsize=(10,8))
plt.boxplot(age_data_clean)
plt.title('Boxplot for Age in IT salary in EU')
plt.ylabel('Age')
plt.show()

