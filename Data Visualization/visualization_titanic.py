import pandas as pd
import matplotlib.pyplot as plt


file_path = "D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Data Visualization/titanic.csv"
data = pd.read_csv(file_path)

# Create a grouped bar chart for 'pclass' and 'survived'
# size(): Đếm số lượng bản ghi (hành khách) trong mỗi nhóm.
"""
.unstack():
Chuyển đổi survived từ dạng chỉ số (index) thành các cột. Kết quả là một bảng (DataFrame) mà:
Các hàng đại diện cho pclass.
Các cột đại diện cho giá trị của survived (0 và 1).
"""
grouped_data = data.groupby(['pclass', 'survived']).size().unstack()

# Plot the grouped data
grouped_data.plot(kind='bar', stacked=False)

# Add chart details
plt.title('Survival Counts by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.legend(['Did Not Survive (0)', 'Survived (1)'], title='Survived')
plt.xticks(rotation=0)

# Show the chart
plt.show()

#tính xác suất điều kiện P(Survived-1|pclass = 3)
# Lọc dữ liệu cho pclass = 3
pclass_3_data = data[data['pclass'] == 3]

# Tổng số hành khách trong pclass = 3
total_pclass_3 = len(pclass_3_data)

# Số hành khách sống sót trong pclass = 3 (Survived = 1)
survived_pclass_3 = len(pclass_3_data[pclass_3_data['survived'] == 1])

# Tính xác suất điều kiện
conditional_probability = survived_pclass_3 / total_pclass_3

print(f"P(Survived = 1 | pclass = 3) = {conditional_probability:.4f}")
print("hay lắm bạn êi")