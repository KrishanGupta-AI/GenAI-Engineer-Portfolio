import numpy as np
import pandas as pd

data = pd.read_csv("DATA VISUALIZATION/Video Games Sales/video_games_sales.csv")
df = pd.DataFrame(data)

print(df.head(5))
print(df.columns)


print(df.info())
print(df.isnull().sum())

print(df.describe)

