import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame( data=iris.data, columns=iris.feature_names)
x = df['sepal length (cm)' ]
df.boxplot(grid=False)
plt.show()