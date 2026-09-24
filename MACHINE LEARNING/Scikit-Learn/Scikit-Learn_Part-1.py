# import pandas as pd
# import numpy  as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Data Preprocessing Funnel : 

# """

# Raw Data
#      ↓
# Handle Missing Data
#      ↓
# Encode Categorical Values
#      ↓
# Feature Scaling
#      ↓
# Split Data
#      ↓
# Prepared Data

# """

# # Handling Missing Data

# import pandas as pd 

# data = {
#     "Name"   : ['Krishan' , 'Rakshit' , 'Alok' , 'Kartik' , 'Kundu'] , 
#     "Age"    : [23 , 34 , 42 , None , None ] , 
#     "Salary" : [90000 , 3400 , None , 302928 , None]
#     }

# Dataframe = pd.DataFrame(data)
# print("Original Data" , Dataframe)

# print(Dataframe.isnull().sum())

# df_drop_data = Dataframe.dropna()
# print("Dataset after handling missing values  \n" ,  df_drop_data)

# Dataframe["Age"]    = Dataframe["Age"].fillna(Dataframe["Age"].mean())
# Dataframe["Salary"] = Dataframe["Salary"].fillna(Dataframe["Salary"].mean())
# print("Updated Dataframe after replacing the missing values with new values. \n" , Dataframe)


# # Encoded Categorical Value
# # Label Encoding : Label Encoding is a technique that converts each unique categorical value into a numerical label (integer).
 
# from sklearn.preprocessing import LabelEncoder 
# # Library used for encoded categorical value is LabelEncoder
# df = pd.read_csv("Scikit-Learn/student_dataset_10000_rows.csv")
# print(df.head(5))

# df_label = df.copy() # Generally , made to preserve the original dataset and make changes on a new one.

# le = LabelEncoder()

# df_label["placement_status_encoded"] = le.fit_transform(df_label["placement_status"]) 
# # Will convert categorical data into numerical numbers (E.g. 0,1,2,3,4,5,6,7,8,9)
# # We created a new column to store the encoded value , such that the original dataset values are not changed and the encoded column can be directly be hand over to the model.
# print(df_label)

# print(df_label[['study_hours' , 'attendance' , 'sleep_hours' , 'placement_status' , 'placement_status_encoded']  ])


# # One-Hot Encoding : One-Hot Encoding is a technique that converts categorical values into multiple binary (0/1) columns, with one column created for each unique category.

# # One-Hot Encoding : 

# df_encoded = pd.get_dummies(df_label , columns = ['internet_usage'])
# print("\n One-Hot Encoded Data (City)")
# print(df_encoded)

# # Practice : To convert One-Hot Encoding column into Label Encoding Column.
# df_encoded['internet_usage_encoded'] = le.fit_transform(df_encoded['internet_usage_11'])
# print(df_encoded['internet_usage_encoded'])



# # Feature Selection and Split Data : 
# from sklearn.preprocessing import MinMaxScaler , StandardScaler
# from sklearn.model_selection import train_test_split

# data_2  = {
#     "Study_Hours" : [1,2,3,4,5,6,7,8,9,10] , 
#     "Test_Score"  : [10,20,30,40,50,60,70,80,90,100]
# }

# df_2 = pd.DataFrame(data_2)

# # Standard Scaler

# standard_scaler = StandardScaler()
# standard_scaled = standard_scaler.fit_transform(df_2)

# print("Standard Scaler Output : ")
# print(pd.DataFrame(standard_scaled , columns = ["Study_Hours" , "Test_score"])) # Feature Scaling

# # Min-Max Scaler

# min_max_scaler = MinMaxScaler()
# min_max_scaled = min_max_scaler.fit_transform(df_2)

# print("\n Min-Max Scaled Output")
# print(pd.DataFrame(min_max_scaled , columns = ["Study_Hours" , "Test_score"])) # Min-Max Scaling


# # Split Data :

# X = data_2["Study_Hours"] # Input
# y = data_2["Test_Score"]  # Output

# X_train , X_test , y_train , y_test  = train_test_split(X , y ,test_size = 0.2 , random_state = 42)

# print("Training Data")
# print(X_train)

# print("Testing Data")
# print(X_test)

# print("Training Data")
# print(y_train)

# print("Testing Data")
# print(y_test)


# print(df.columns)

# # SUPERVISED MACHINE LEARNING :

# # LINEAR REGRESSION :  y = mx + c


# from sklearn.linear_model import LinearRegression
# model = LinearRegression()

# X = df[['study_hours']]
# y = df['exam_score']

# model.fit(X , y)

# value = float(input("How many hours did you study ?"))
# predicted_marks = model.predict(pd.DataFrame([[value]] , columns = ['study_hours']))
# print("Based on number of hours you studied , you might score : " , predicted_marks)



# # LOGISTIC REGRESSION :  σ(z) = 1 / (1 + e^(-z)) 
# # Output lies in range  :  0 to 1 (0 ---> NO  , 1 ---> YES)

# from sklearn.linear_model import LogisticRegression

# X = [[1],[2],[3],[4],[5]] # Hour studied input (Feature)
# y = [0,0,1,1,1] # Output  (0 ---> Fail , 1 ---> Pass)

# model = LogisticRegression()
# model.fit(X,y)

# hours = float(input("Enter how many hours did you study ?"))

# result  = model.predict([[hours]]) [0] 
# # model.predict() returns an array:
# # [0] extracts the first prediction:

# if result == 1:
#     print("You might get pass.")
# else :
#     print("You might get fail.")    





# # KNN (K-Nearest Neighbour) : 

# from sklearn.neighbors import KNeighborsClassifier

# X = [ #weight , size
#     [180,7],
#     [200,7.5],
#     [250,8],
#     [300,8.5],
#     [330,9],
#     [360,9.5]
# ]

# # 0 ---> Apple  , 1 ---> Orange
# y = [0,0,0,1,1,1]

# model = KNeighborsClassifier(n_neighbors = 5)
# model.fit(X , y)

# weight = float(input("Enter the weight in grams : "))

# size = float(input("Enter the size in cm : "))

# prediction = model.predict([[weight , size]]) [0]

# if prediction == 0:
#     print("This is likely an Apple")
# else :
#     print("This is likely an Orange")




# # DECISION TREE : A Decision Tree is a supervised Machine Learning algorithm that makes predictions by repeatedly splitting data based on feature values, forming a tree-like structure of decisions.

# from sklearn.tree import DecisionTreeClassifier

# X = [ #size , shade
#     [180,7],
#     [200,7.5],
#     [250,8],
#     [300,8.5],
#     [330,9],
#     [360,9.5]
# ]

# # 0 ---> Apple  , 1 ---> Orange
# y = [0,0,0,1,1,1]

# model = DecisionTreeClassifier()
# model.fit(X , y)

# size = float(input("Enter the size in cm : "))
# shade = float(input("Enter the color shade(1 - 10) : "))

# result = model.predict([[size , shade]]) [0]

# if result == 0:
#     print("This is likely an Apple")
# else :
#     print("This is likely an Orange")


# # fit()
# # → Used to train the model by learning patterns/relationships from the training data.
# # → Generally used during the training phase.
# # → Usually called once for a given training process.

# # predict()
# # → Used to make predictions/output using the trained model.
# # → Can be called multiple times on different/new data.
# # → Used on unseen data as well as for generating predictions from existing data.


# # TYPES OF FITTING :

# # Overfitting
# # → Very smart but foolish.
# # → Performs very well on training data but poorly on unseen/test data.
# # → Model memorizes the training data instead of learning general patterns.

# # Underfitting
# # → Not smart and not intelligent.
# # → Performs poorly on both training and test data.
# # → Model is too simple to learn the underlying patterns.

# # Good Fit
# # → Smart and sensible.
# # → Performs well on both training and unseen/test data.
# # → Model learns the important patterns without memorizing the training data.



# # MODEL EVALUATION : Model Evaluation is the process of measuring how well a trained Machine Learning model performs on unseen data using appropriate evaluation metrics.

# # MASTERING MODEL EVALUATION :
# # 1.) Skelarn Metrics
# # 2.) Regression Metrics
# # 3.) Confusion Metrics
# # 4.) Classification Metrics


# # 4.) Classification Metrics : Learn to evaluate classification models using accuracy , precision , recall and F-1 Score.

# # Classification Evaluation Metrics

# # 1. Accuracy : Accuracy measures the proportion of total predictions that are correctly classified by the model.

# # Formula : Accuracy = (True Positive + True Negative) / (True Positive + True Negative + False Positive + False Negative)

# # In simple words : Accuracy tells us how many predictions the model got correct out of all predictions.


# # 2. Precision : Precision measures the proportion of correctly predicted positive observations among all observations predicted as positive.

# # Formula : Precision = True Positive / (True Positive + False Positive)

# # In simple words : Out of all the cases predicted as Positive, how many were actually Positive?


# # 3. Recall : Recall measures the proportion of correctly identified positive observations among all actual positive observations.

# # Formula : Recall = True Positive / (True Positive + False Negative)

# # In simple words : Out of all the actual Positive cases, how many did the model correctly identify?


# # 4. F1-Score : F1-Score is the harmonic mean of Precision and Recall. It provides a balance between Precision and Recall.

# # Formula : F1-Score = 2 × (Precision × Recall) / (Precision + Recall)

# # In simple words : F1-Score provides a single measure that balances Precision and Recall.


# # Quick Revision : 
# # Accuracy  → Overall correctness of the model.
# # Precision → Correctness of Positive predictions.
# # Recall    → Ability to identify actual Positive cases.
# # F1-Score  → Balance between Precision and Recall.

# from sklearn.metrics import accuracy_score , precision_score , f1_score , recall_score

# # True answers (What actually happened)
# y_true = [1,0,1,1,0,1,0]

# # Model's prediction (What it guessed)
# y_pred = [1,0,1,0,0,1,1]

# # Evaluation
# print("Accuracy : " , accuracy_score(y_true , y_pred)) # Accuracy is not just enough if the dataset is biased or unbalanced.
# print("Precision : " , precision_score(y_true , y_pred))
# print("Recall : " , recall_score(y_true , y_pred))
# print("f1 score : " , f1_score(y_true , y_pred))



# Confusion Metrics : Understand how to use a confusion matrix to analyze model performance.

from sklearn.metrics import confusion_matrix

y_true = [1,0,1,1,0,1,0,0,1,0]
y_pred = [1,0,1,0,0,1,1,0,1,0]

cm = confusion_matrix(y_true , y_pred)

print("Confusion Matrix")

print(cm) 

# Output : 
# True Positive               False Positive
# False Negative              True Negative



# Regression Metrics : Learn to evaluate regression models using MAE , MSE and RMSE.

# 1. Mean Absolute Error (MAE) :  Mean Absolute Error measures the average absolute difference between the actual values and the predicted values.

# Formula : Mean Absolute Error = Σ |Actual Value - Predicted Value| / Number of Observations

# In simple words : It tells us, on average, how far the model's predictions are from the actual values.

# Lower MAE = Better Model


# ------------------------------------------------------------

# 2. Mean Squared Error (MSE) : Mean Squared Error measures the average of the squared differences between the actual values and the predicted values.

# Formula :  Mean Squared Error = Σ (Actual Value - Predicted Value)² / Number of Observations

# In simple words : It measures prediction error and gives greater importance to larger errors because the errors are squared.

# Lower MSE = Better Model


# ------------------------------------------------------------

# 3. Root Mean Squared Error (RMSE) : Root Mean Squared Error is the square root of the Mean Squared Error and measures the typical magnitude of prediction errors.

# Formula : Root Mean Squared Error = √[Σ (Actual Value - Predicted Value)² / Number of Observations]

# In simple words : It tells us the typical size of the prediction error in the same unit as the target variable.

# Lower RMSE = Better Model


# ------------------------------------------------------------

# 4. R² Score (Coefficient of Determination) : R² Score measures how well the model explains the variation in the actual target values.

# Formula : R² Score = 1 - [Σ (Actual Value - Predicted Value)² / Σ (Actual Value - Mean of Actual Values)²]

# In simple words : It tells us how much of the variation in the target variable is explained by the model.

# R² Score = 1
# → Perfect Model

# R² Score = 0
# → Model explains no more variation than simply predicting the mean.

# R² Score < 0
# → Model performs worse than predicting the mean.

# Higher R² Score = Generally Better Model
 

from sklearn.metrics import mean_absolute_error , mean_squared_error
import numpy as np

# real scores
real_scores = [90 , 60 , 80 , 100]

# model guess
predicted_scores = [85 , 70 , 70 , 95]

mae = mean_absolute_error(real_scores , predicted_scores)

mse= mean_squared_error(real_scores ,  predicted_scores)

rmse = np.sqrt(mse)

print("MAE : On average off by : " , mae)
print("MSE : Squared Mistake Value : " , mse)
print("RMSE : Final Reliastic Error : " , rmse)


# Sklearn Metrics : Master the use of "Sklearn.metrics" for comprehensive model evaluation.




