import seaborn as sns

planets = sns.load_dataset('planets')

print(planets.shape)

print(planets.head())


"""Cột 'method' chứa thông tin về phương pháp được sử dụng để phát hiện 
các hành tinh trong dataset, và nunique() đếm số lượng các giá trị duy nhất trong cột này.

Vì vậy, số 10 có nghĩa là có 10 phương pháp khác nhau đã được sử dụng 
để phát hiện các hành tinh trong tập dữ liệu "planets"."""

print(planets['method'].nunique())


print(planets.groupby('method')['year'].describe())