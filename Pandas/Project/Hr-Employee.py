import pandas as pd 

df = pd.read_csv("Project/WA_Fn-UseC_-HR-Employee-Attrition.csv")
print(df.head(5))

print(df.columns)
print(df.shape)