from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[3, 0, 110], [2, 1, 90], [4, 1, 120], [
             4, 0, 140], [2, 0, 100], [2, 1, 80], [3, 0, 100]])
Y = np.array([[1450], [1000], [1850], [2200], [1100], [850], [1300]])

model = LinearRegression().fit(X, Y)

# Y= ax+b
print(model.predict(np.array([[3, 1, 140]])))
