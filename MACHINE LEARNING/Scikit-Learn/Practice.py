import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Scikit-Learn/student_dataset_10000_rows.csv")

df = pd.DataFrame(data)
print(df.head(5))

print(df.columns)

print(df.isnull().sum())

from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df["placement_status_encoded"] = le.fit_transform(df['placement_status'])

print(df["placement_status_encoded"])

from sklearn.preprocessing import MinMaxScaler , StandardScaler

standard_scalar = StandardScaler()
standard_scaled = standard_scalar.fit_transform(df[["sleep_hours" , "exam_score"]])

print(pd.DataFrame(standard_scaled , columns = ["sleep_hours" , "exam_score"]))

from sklearn.model_selection import train_test_split

X = df[["sleep_hours" , "exam_score"]]
y = df["placement_status"]

X_train , X_test , y_train , y_test = train_test_split(X , y , test_size = 0.2 , random_state = 42)


print("Training Data")
print(X_train)

print("Testing Data")
print(X_test)

print("Training Data")
print(y_train)

print("Testing Data")
print(y_test)



#  SUPERVISED MACHINE LEARNING :

# Linear Regression :  y = mx + c



# Step-by-Step Machine Learning Project Workflow

# Step-1 : Load and Understand data.[Gather and analyze the dataset to understand its structure and content.]

# Step-2 : Preprocessing(Clean Data).[Handle Missing Values , outliers , and inconsitencies to ensure data quality.]

# Step-3 : Feature Scaling(if needed).[Normailze or Standardize features to improve model performance.]

# Step-4