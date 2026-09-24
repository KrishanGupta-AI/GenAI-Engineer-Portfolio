import numpy as np
import pandas as pd

data = pd.read_csv("Machine Learning/House Prediction Model/data-selected-columns.csv")
df = pd.DataFrame(data)

print(df.head(5))
print(df.columns)


print(df.info())
print(df.isnull().sum())

print(df.describe)

