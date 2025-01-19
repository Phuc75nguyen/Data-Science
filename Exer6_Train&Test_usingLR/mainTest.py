from matplotlib import pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

from utils.data_preprocessing import load_data, preprocess_2018, preprocess_2019, preprocess_2020, merge_data
from utils.encoding import fill_nan_with_mean_or_freq, standardize_columns, ordinal_encode_level, one_hot_encode_columns
from utils.standardization import standardize_experience, standardize_vacation_days

# File paths to data
file_paths = [
    'D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Exer6_Train&Test_usingLR/data/IT_Salary_Survey_EU_2018.csv',
    'D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Exer6_Train&Test_usingLR/data/IT_Salary_Survey_EU_2019.csv',
    'D:/COMPUTER SCIENCE PTITHCM/PYTHON4AI/Data Science/Exer6_Train&Test_usingLR/data/IT_Salary_Survey_EU_2020.csv'
]

# Load and preprocess data
dfs = load_data(file_paths)
dfs[0] = preprocess_2018(dfs[0])
dfs[1] = preprocess_2019(dfs[1])
dfs[2] = preprocess_2020(dfs[2])
df_merged = merge_data(dfs)

# Fill missing data and standardize columns
fill_nan_with_mean_or_freq(df_merged, 'Age')
fill_nan_with_mean_or_freq(df_merged, 'Gender', 'freq')
fill_nan_with_mean_or_freq(df_merged, 'City', 'freq')
fill_nan_with_mean_or_freq(df_merged, 'Position', 'freq')
standardize_columns(df_merged)
standardize_experience(df_merged)
standardize_vacation_days(df_merged)
ordinal_encode_level(df_merged)
df_encoded = one_hot_encode_columns(df_merged)

# Loại bỏ các hàng có NaN trong cột salary
df_encoded = df_encoded.dropna(subset=['salary'])

# Tách dữ liệu
X = df_encoded.drop(columns=['salary'])
y = df_encoded['salary']
X = X.apply(pd.to_numeric, errors='coerce').fillna(0)  # Chuyển đổi tất cả sang kiểu số, điền NaN nếu có

# Chia tập dữ liệu
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train and evaluate Linear Regression model
lr_model = LinearRegression()
lr_model.fit(X_train_scaled, y_train)

y_train_pred = lr_model.predict(X_train_scaled)
y_test_pred = lr_model.predict(X_test_scaled)

train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

print(f"Train MSE: {train_mse}")
print(f"Test MSE: {test_mse}")
print(f"Train R2: {train_r2}")
print(f"Test R2: {test_r2}")

# Vẽ biểu đồ cho biến main tech
plt.figure(figsize=(10, 8))  # Tăng kích thước biểu đồ

# Lấy danh sách các công nghệ
main_techs = [col for col in X.columns if col.startswith('main tech_')]

# Vẽ biểu đồ cho từng công nghệ
for tech in main_techs:
    tech_mask = X_test[tech] == 1  # Chọn công nghệ cụ thể
    plt.scatter(X_test[tech_mask]['Years of experience'], y_test[tech_mask], label=f'True Salary - {tech}', alpha=0.5)
    plt.plot(X_test[tech_mask]['Years of experience'], y_test_pred[tech_mask], label=f'Predicted Salary - {tech}', linewidth=2)

plt.xlabel('Years of Experience', fontsize=14)  # Tăng kích thước chữ
plt.ylabel('Salary', fontsize=14)  # Tăng kích thước chữ
plt.title('Salary vs Years of Experience by Main Technology', fontsize=16)  # Tăng kích thước chữ

# Điều chỉnh kích thước và vị trí của phần chú thích
plt.legend(fontsize='small', loc='upper left', bbox_to_anchor=(1, 1), frameon=True, title="Legend")  # Đặt chú thích bên ngoài

plt.grid()
plt.tight_layout()
plt.show()

