import pandas as pd
import matplotlib.pyplot as plt


file_path = "D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Data Visualization/births.csv"
data = pd.read_csv(file_path)

# Tổng hợp dữ liệu sinh theo từng năm
births_per_year = data.groupby('year')['births'].sum()

# Vẽ biểu đồ
plt.figure(figsize=(12,6))
plt.plot(births_per_year.index, births_per_year.values, marker='o', color='b')
plt.title('The Number of Births per Year (1969-2008)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Births', fontsize=12)

# hiển thị 1969 và 2008
plt.xlim(1969, 2008)

plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
