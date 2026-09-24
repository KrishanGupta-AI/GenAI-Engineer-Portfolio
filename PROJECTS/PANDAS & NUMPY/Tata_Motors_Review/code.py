import pandas as pd
import numpy as np

data = pd.read_csv("PANDAS & NUMPY/Tata_Motors_Review_Dataset/Tata_Motors_Employee_Reviews_from_AmbitionBox.csv")
print(data.head(5))

print(data.columns)
# print(data.info())

print(data.isnull().sum())

data["Overall_rating"]= data["Overall_rating"].fillna(data["Overall_rating"].mean())

