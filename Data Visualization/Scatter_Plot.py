import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.feature_names)
print(iris.target_names)
print(iris.data.shape)
print(iris.data.T.shape)

features = iris.data.T
plt.scatter(features[0], features[1], s=20, c=iris.target)
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.show()