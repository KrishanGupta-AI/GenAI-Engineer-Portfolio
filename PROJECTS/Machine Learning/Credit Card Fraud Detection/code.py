import numpy as np
import pandas as pd

data = pd.read_csv("Machine Learning/Credit Card Fraud Detection/fraud_detection_credit_card_small.csv")
df = pd.DataFrame(data)

print(df.head(5))
print(df.columns)


print(df.info())
print(df.isnull().sum())

print(df.describe)

