import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print("Miniconda environment works")

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

model = LinearRegression()
model.fit(x, y)

print("Prediction for x=6:", model.predict([[6]]))
print("R^2 score:", model.score(x, y))