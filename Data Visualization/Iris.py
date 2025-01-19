import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=[iris.feature_names])

df['Species'] = iris['target'] #thêm một cột vào data frame tên là Species
xs = [i + 0.1 for i, _ in enumerate(iris.target_names)]

plt.bar(xs, df["Species"].value_counts().to_numpy())

plt.xticks([i + 0.5 for i, _ in enumerate(iris.target_names)], iris.target_names)
plt.ylabel("# of each species" )
plt.title("Species")
plt.show()