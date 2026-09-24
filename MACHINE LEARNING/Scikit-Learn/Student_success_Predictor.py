# Steps of building a Machine Learning Model

# Load & Understand the Data
#           ↓
# Preprocessing (Clean Data)
#           ↓
# Feature Scaling
#           ↓
# Split the Data
#           ↓
# Train a Model
#           ↓
# Make Predictions
#           ↓
# Evaluate the Model
#           ↓
# Visualize the Results
#           ↓
# Improve / Experiment
#           ↓
# Wrap-Up


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# --------------------------------------------------
# LOAD & UNDERSTAND THE DATA
# --------------------------------------------------

data = pd.read_csv("Scikit-Learn/StudentPerformanceFactors.csv")

df = pd.DataFrame(data)


print("Sample Rows")
print(df.head(5))


print("Dataset Shape")
print(f'Rows : {df.shape[0]} , Columns : {df.shape[1]}')


print("All Column Names")
print(df.columns)


print("Dataset Info")
print(df.info())


print("Summary Statistics")
print(df.describe(include='all'))


print("Missing Values")
print(df.isnull().sum())


# --------------------------------------------------
# PREPROCESSING (CLEAN DATA)
# --------------------------------------------------

print(df[['Teacher_Quality' , 'Parental_Education_Level' , 'Distance_from_Home']])

# These columns contain missing categorical values.
# We will fill the missing values using the mode.

categorical_columns = ['Teacher_Quality' , 'Parental_Education_Level' , 'Distance_from_Home']


for column in categorical_columns:

    df[column] = df[column].fillna(df[column].mode()[0])


print("Missing Values After Cleaning")
print(df[categorical_columns].isnull().sum())


# --------------------------------------------------
# LABEL ENCODING
# --------------------------------------------------

teacher_encoder = LabelEncoder()

internet_encoder = LabelEncoder()


df["Teacher_Quality_encoded"] = teacher_encoder.fit_transform(df["Teacher_Quality"])

df["Internet_Access_encoded"] = internet_encoder.fit_transform(df["Internet_Access"])

print("Encoded Teacher Quality")
print(df["Teacher_Quality_encoded"])


print("Encoded Internet Access")
print(df["Internet_Access_encoded"])


# --------------------------------------------------
# CREATE PASS / FAIL TARGET
# --------------------------------------------------

# Exam_Score ranges from approximately 55 to 101
# in this dataset.
#
# Therefore, using 50 as the passing threshold
# would make every student a Pass.
#
# We are using 70 as a learning threshold:
#
# 1 = Pass
# 0 = Fail

df["Pass_Fail"] = np.where(df["Exam_Score"] >= 70 , 1 , 0)

print("Pass / Fail Distribution")
print(df["Pass_Fail"].value_counts())


# --------------------------------------------------
# SELECT FEATURES
# --------------------------------------------------

features = ["Hours_Studied" , "Internet_Access_encoded" , "Teacher_Quality_encoded"]

X = df[features]

y = df["Pass_Fail"]


# --------------------------------------------------
# SPLIT THE DATA
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(X , y , test_size = 0.2 , random_state = 42 , stratify = y)


# --------------------------------------------------
# FEATURE SCALING
# --------------------------------------------------

scaler = StandardScaler()

# Fit scaler only on training data
# to avoid data leakage.

X_train_scaled = scaler.fit_transform(X_train)


# Only transform test data.

X_test_scaled = scaler.transform(X_test)


# --------------------------------------------------
# TRAIN A MODEL
# --------------------------------------------------

model = LogisticRegression()

model.fit(X_train_scaled , y_train)


# --------------------------------------------------
# MAKE PREDICTIONS
# --------------------------------------------------

y_prediction = model.predict(X_test_scaled)


# --------------------------------------------------
# EVALUATE THE MODEL
# --------------------------------------------------

print("Accuracy")

print(accuracy_score(y_test , y_prediction))

print("Classification Report")
print(classification_report(y_test , y_prediction))


# --------------------------------------------------
# CONFUSION MATRIX
# --------------------------------------------------

conf_matrix = confusion_matrix(y_test , y_prediction)

plt.figure(figsize=(6, 4))

sns.heatmap(conf_matrix , annot=True , fmt='d' , cmap="Blues" , xticklabels=["Fail", "Pass"] , yticklabels=["Fail", "Pass"])

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.tight_layout()
plt.show()


# --------------------------------------------------
# PREDICT YOUR RESULT
# --------------------------------------------------

print("------- Predict Your Result -------")

try:

    hours_studied = float(input("Enter study hours: "))

    internet_access = input("Enter Internet Access (Yes/No): ")

    teacher_quality = input("Enter Teacher Quality (Low/Medium/High): ")

    # Encode Internet Access

    internet_access_encoded = internet_encoder.transform([internet_access])[0]

    # Encode Teacher Quality

    teacher_quality_encoded = teacher_encoder.transform([teacher_quality])[0]

    # Create user input DataFrame

    user_input_df = pd.DataFrame([[hours_studied , internet_access_encoded , teacher_quality_encoded]] , columns=features)

    # Scale user input

    user_input_scaled = scaler.transform(user_input_df)

    # Make prediction

    prediction = model.predict(user_input_scaled)[0]

    # Convert prediction into Pass / Fail

    result = "Pass" if prediction == 1 else "Fail"

    print("Prediction based on Input:" , result)

except Exception as e:

    print("An error has occurred:" , e)