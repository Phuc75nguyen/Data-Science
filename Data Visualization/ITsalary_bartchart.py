"""
Thống kê số lượng nhân viên theo giới tính của từng năm.
Minh hoạ phần thống kê trên dùng biểu đồ cột.

Lưu ý: 
Sinh viên làm bài theo nhóm, sinh viên có mã số thấp nhất sẽ đại diện nhóm nộp bài. 
File nộp có tên MaSV.zip với MaSV là mã sinh viên thấp nhất của nhóm. File nén chứa các file sau:
- MaSV.py   : file code 
- MaSV.csv : file dữ liệu
"""


import matplotlib.pyplot as plt
import pandas as pd

#đọc 3 file IT survey 18-19-20
df_2018 = pd.read_csv("D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Data Visualization/IT_Salary_Survey_EU_2018.csv")
df_2019 = pd.read_csv("D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Data Visualization/IT_Salary_Survey_EU_2019.csv")
df_2020 = pd.read_csv("D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Data Visualization/IT_Salary_Survey_EU_2020.csv")


#nối 3 file lại bằng hàm concat()
data_IT_combined = pd.concat([df_2018, df_2019, df_2020], ignore_index=True)

#Chuyển cột TimeStamp thành Datetime theo gợi ý của cô => dễ lấy dữ liệu của từng năm
#dùng hàm .to_datetime()
#data_IT_combined = pd.to_datetime(data_IT_combined['Timestamp'], errors= 'coerce')
#dayfirst=True: giúp tránh cảnh báo về định dạng ngày tháng khi ngày đến trước tháng trong dữ liệu.
data_IT_combined['Timestamp'] = pd.to_datetime(data_IT_combined['Timestamp'], errors='coerce', dayfirst=True)

#Tạo lại cột year, truy xuất từ Timestamp ở trên: 
# Sử dụng .dt.year để lấy năm từ cột Timestamp
data_IT_combined['year'] = data_IT_combined['Timestamp'].dt.year
# Lọc dữ liệu chỉ lấy năm 2018, 2019 và 2020
data_IT_combined = data_IT_combined[data_IT_combined['year'].isin([2018, 2019, 2020])]



#Test ket qua
#print(genders_per_years)
#Ket qua cho ra data lộn xộn, có thêm cột Diverse M F
"""Gender  Diverse     F  Female      M    Male
Gender  Diverse     F  Female      M    Male
year
2018.0      NaN  98.0     NaN  608.0     NaN
2019.0      NaN   6.0     NaN   31.0     NaN
2020.0      2.0   1.0   189.0    7.0  1016.0
2021.0      NaN   NaN     3.0    NaN    33.0"""



# Ta chuẩn hóa cột Gender chỉ giữ lại 'Male' và Female
data_IT_combined['Gender'] = data_IT_combined['Gender'].replace({
    'M': 'Male', 'F': 'Female', 'Diverse': None, 'Other': None
}).dropna()

#Thống kê gender theo year
genders_per_years = data_IT_combined.groupby(['year', 'Gender']).size().unstack()
#print test lại
print(genders_per_years)

# Lưu kết quả thống kê vào file CSV
genders_per_years.to_csv('D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Data Visualization/IT_Salary_Survey_Statistics.csv', index=True)

print("Đã lưu kết quả thống kê vào file CSV.")


#ve bieu do cot cho year & gender trong bo du lieu tren
genders_per_years.plot(kind='bar', figsize=(12, 8))
plt.title('Number of employees Gender per year')
plt.xlabel("Year")
plt.ylabel("Number of Employees")
plt.xticks(rotation = 0)
plt.legend(title = "Gender")
plt.show()