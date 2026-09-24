# Scikit-learn ---> Scikit-learn is an open-source Python machine learning library used for data preprocessing, building, training, evaluating, and deploying traditional machine learning models.

# ------------------------------------------------------------

# Use Cases -- Scikit-learn is mainly used for :

# • Data preprocessing and cleaning
# • Feature engineering
# • Classification
# • Regression
# • Clustering
# • Dimensionality reduction
# • Model selection
# • Model evaluation
# • Hyperparameter tuning

# ------------------------------------------------------------

# Advantages

# • Easy to learn and use.
# • Provides many machine learning algorithms.
# • Works well with NumPy, Pandas, and Matplotlib.
# • Provides tools for data preprocessing.
# • Provides built-in model evaluation metrics.
# • Supports pipelines for efficient ML workflows.
# • Well documented and widely used.
# • Suitable for both beginners and professionals.

# ------------------------------------------------------------

# Applications

# • Fraud Detection
# • Spam Detection
# • Customer Churn Prediction
# • House Price Prediction
# • Customer Segmentation
# • Recommendation Systems
# • Sentiment Analysis
# • Credit Risk Prediction
# • Disease/Medical Prediction
# • Sales and Demand Prediction

# ------------------------------------------------------------

# Major Algorithms Available

# Supervised Learning

# Classification:
# • Logistic Regression
# • K-Nearest Neighbors (KNN)
# • Decision Tree
# • Random Forest
# • Support Vector Machine (SVM)
# • Naive Bayes

# Regression:
# • Linear Regression
# • Polynomial Regression
# • Decision Tree Regressor
# • Random Forest Regressor
# • SVR

# Unsupervised Learning

# • K-Means Clustering
# • DBSCAN
# • Hierarchical Clustering
# • PCA (Principal Component Analysis)

# ------------------------------------------------------------

# Important Modules

# • sklearn.preprocessing → Data preprocessing
# • sklearn.model_selection → Train-test split, cross-validation, GridSearchCV
# • sklearn.linear_model → Linear & Logistic Regression
# • sklearn.tree → Decision Trees
# • sklearn.ensemble → Random Forest, Gradient Boosting
# • sklearn.metrics → Model evaluation
# • sklearn.cluster → Clustering
# • sklearn.decomposition → Dimensionality reduction
# • sklearn.pipeline → ML pipelines

# ------------------------------------------------------------

# Simple Example :

# ******
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42 )

# model = LinearRegression()
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# ******


# Why should I focus on mathematics in Data Science?
# 1.) To understand models ---> Gain insight into model functionality to avoid blind usage.
# 2.) Debug Effectively ---> Fix errors and improve model performance.
# 3.) Train as a real Scientist ---> Develop critical thinking and independence. 



# Mean          ---> The mean is the sum of all values in a dataset divided by the total number of values
# Median        ---> The median is the middle value of a dataset when the data is arranged in ascending or descending order.(If there are an even number of values, the median is the average of the two middle values.)
# Mode          ---> The mode is the value that occurs most frequently in a dataset.
# Percentages   ---> Expressing numbers as part of 100.
# Ratios        ---> Comparing two or more quantities.= 
# Basic Algebra ---> Solving Equations with variables. (y = mx + b)
""" 

y  =  output
x  =  input 
m  =  rate of change 
b  =  starting point 

"""


# Plotting X vs Y ----> Plotting X vs Y means visualizing how Y changes with respect to X.
"""

x ---> independent variable input
y ---> dependent variable (output in 99% cases)

"""

# Vectors      ----> Quantities with both magnitude and direction.
# In Machine Learning , "A vector is a list of numbers that represents the features or characteristics of an observation."


# Standard Deviation    ---> Standard Deviation is a statistical measure that tells us how much the values in a dataset are spread out or how far they typically are from the mean.

"""

Low Standard Deviation:
→ Data values are close to the mean.
→ Less variation.

High Standard Deviation:
→ Data values are far from the mean.
→ More variation.

"""

# Probability  ---> Probability is a measure of how likely or unlikely an event is to occur.


# General Terms in Machine Learning : 

# Actual       ---->  The actual value is the true or real outcome of an observation in the dataset, against which the model's prediction is compared.


# Predictive   ----> The predicted value is the outcome that a machine learning model estimates or predicts for an observation.


# Accuracy      ----> Accuracy is a classification evaluation metric that measures the proportion of correctly predicted observations out of the total number of observations.
# Accuracy = (Correct Predictions / Total Predictions) × 100


# Precision     ----> Precision measures how many of the observations predicted as Positive by the model are actually Positive.
# Precision = (True Positives / Total Predictive Positives)


# Recall        ----> Recall measures how many of the actual Positive observations were correctly identified by the model.
# Recall = (True Positives / Total Actual Positives)


# Machine Learning (ML): Machine Learning is a branch of Artificial Intelligence that enables 
# computers to learn patterns from data and make predictions or decisions without being explicitly 
# programmed for every task.


# Artificial Intelligence (AI): Artificial Intelligence is a branch of computer science that enables
# machines to perform tasks that typically require human intelligence, such as learning, reasoning,
# problem-solving, perception, and decision-making.


# Deep Learning: Deep Learning is a subset of Machine Learning that uses multi-layered artificial
# neural networks to automatically learn complex patterns and representations from large amounts
# of data.


# Types of Machine Learning
# Machine Learning is mainly divided into 4 types:

# 1. Supervised Learning
# 2. Unsupervised Learning
# 3. Semi-Supervised Learning
# 4. Reinforcement Learning

# ------------------------------------------------------------

# 1. Supervised Learning (Ideal for tasks with labelled data where the desired output is unkonown).

# Definition:
# Learning from labeled data, where the model learns the relationship between input (X) and known output (Y).

# Main Tasks:
# • Classification
# • Regression

# Examples:
# • Spam Detection
# • House Price Prediction
# • Disease Prediction

# ------------------------------------------------------------

# 2. Unsupervised Learning (Suitable for identifying patterns in unlabelled data without explicit guidance).

# Definition:
# Learning from unlabeled data, where the model finds hidden patterns, structures, or groups in the data without a predefined output.

# Main Tasks:
# • Clustering
# • Dimensionality Reduction
# • Association

# Examples:
# • Customer Segmentation
# • Anomaly Detection
# • Data Pattern Discovery

# ------------------------------------------------------------

# 3. Semi-Supervised Learning

# Definition:
# Learning from a combination of a small amount of labeled data and a large amount of unlabeled data.

# Example:
# A small number of labeled images + thousands of unlabeled images used to train a model.

# Applications:
# • Image Classification
# • Speech Recognition
# • Web Content Classification

# ------------------------------------------------------------

# 4. Reinforcement Learning (Best for training agents to make decisions through interaction with an enviorment).

# Definition:
# A type of Machine Learning where an agent learns by interacting with an environment and receiving rewards or penalties for its actions.

# Main Components:
# • Agent
# • Environment
# • Action
# • Reward
# • State

# Examples:
# • Game Playing
# • Robotics
# • Autonomous Vehicles
# • Recommendation/Decision Systems

# ------------------------------------------------------------

# Easy Way to Remember

# Supervised       → Labeled Data → Learn X → Y

# Unsupervised     → Unlabeled Data → Find Patterns

# Semi-Supervised  → Labeled + Unlabeled Data

# Reinforcement    → Actions + Rewards/Penalties

# ------------------------------------------------------------

# Interview Answer

# "The four major types of Machine Learning are Supervised Learning, Unsupervised Learning, Semi-Supervised Learning, and Reinforcement Learning. They differ mainly in how the model receives feedback or training information."



# Core ML concepts overview : 

# 1.) Input(X)   ---> Input (X) represents the features or independent variables provided to a Machine Learning model to make a prediction or determine an output (y).
                    # X = Input/Features  Y = Output/Target.
                    # X is always capital as it can refer multiple columns or features at once.

# 2.) Output(y)  ---> Output (y) represents the target or dependent variable that a Machine Learning model predicts based on the input features (X).
                    # Y = Output/Target.
                    # y is small as it is generally the output which we are trying to find.

# 3.) Model      ---> A Machine Learning model is a trained mathematical representation that learns patterns from data and uses them to make predictions or decisions on new data.

# 4.) Testing    ---> Testing is the process of evaluating a trained Machine Learning model on unseen data to measure how well it performs on new, previously unseen examples.

# 5.) Training   ---> Training is the process of teaching a Machine Learning model to learn patterns and relationships from training data by adjusting its parameters to make accurate predictions.

# 6.) Prediction ---> Prediction is the output or estimated result produced by a Machine Learning model based on the given input data (X).


# Why Should We Learn Scikit-learn?

# * Easy-to-use Python library for Machine Learning.
# * Provides many ML algorithms.
# * Helps with data preprocessing and feature engineering.
# * Provides model evaluation metrics like Accuracy, Precision, Recall, and F1-score.
# * Supports train-test splitting and cross-validation.
# * Helps with hyperparameter tuning.
# * Supports ML pipelines.
# * Works well with NumPy, Pandas, Matplotlib, and Seaborn.
# * Useful for building real-world ML projects.
# * Helps build strong Machine Learning fundamentals for AI/GenAI.


# Data Preprocessing Funnel : 

"""

Raw Data
     ↓
Handle Missing Data
     ↓
Encode Categorical Values
     ↓
Feature Scaling
     ↓
Split Data
     ↓
Prepared Data

"""

# 1. Raw Data ---> Raw data is the original data collected from various sources before any cleaning or preprocessing.

# 2. Handle Missing Data ---> Identify and handle missing values by:

# Removing missing values
# Filling them with appropriate values
# Using techniques such as mean, median, or mode imputation

# 3. Encode Categorical Values ---> Convert categorical values into numerical values so that Machine Learning algorithms can process them.
# Examples:

# Label Encoding
# One-Hot Encoding

# 4. Feature Scaling ---> Transform numerical features to a similar scale so that features with larger values do not dominate the model.
# Common techniques:

# Standardization
# Normalization

# 5. Split Data ---> Divide the prepared dataset into different subsets, mainly:

# Training Data → Used to train the model.
# Testing Data → Used to evaluate the model.

# Common split:
# 80% → Training
# 20% → Testing

# 6. Prepared Data ---> The final clean and transformed data that is ready to be given to a Machine Learning model.


# Why Do We Handle Missing Values?

# *To avoid errors while training Machine Learning models.
# *To improve data quality and reliability.
# *To prevent loss of important information.
# *To ensure accurate analysis and predictions.
# *Many ML algorithms cannot directly handle missing values.
# *To maintain consistency** in the dataset.
# *To prevent biased or incorrect results caused by missing data.

# Easy method to handle missing value : 
# .dropna()  ---> Removes all the rows (complete rows) with even a single missing value.

# .fillna()  ---> Fills empty values with the values we need.

# Check percentage of missing data by  data.isnull().mean() * 100 
# Before using dropna() function , always try to replace the missing value with mean or median if possible for numerc data.
# For categorical data , try the mode function to handle missing data.


# Encoded Categorical Value ---> Encoding categorical values is the process of converting categorical (text-based) data into numerical values so that Machine Learning algorithms can process them.

# Common Encoding Techniques
# Label Encoding → Assigns a numerical value to each category.
# One-Hot Encoding → Creates separate binary (0/1) columns for each category.



# Feature Scaling  ---> Feature Scaling is the process of transforming numerical features to a similar scale so that features with larger numerical values do not disproportionately influence the Machine Learning model.
# Common Techniques : 

# 1. Standardization  ----> Standardization is a feature scaling technique that transforms data so that it has a mean of 0 and a standard deviation of 1.
# Syntax : 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform()



# 2. Normalization (Min-Max Scaling)  ----> Normalization is a feature scaling technique that transforms numerical values to a fixed range, typically 0 to 1.
# Syntax : 
from sklearn.preprocessing import MinMaxScaler
scaler_1 = MinMaxScaler()
X_scaled_1 = scaler_1.fit_transform()



# Split Data: Splitting data is the process of dividing a dataset into separate subsets,
# mainly training data for learning the model and testing data for evaluating its performance on unseen data.

# Syntax : 
from sklearn.model_selection import train_test_split


# SUPERVISED MACHINE LEARNING : Supervised Machine Learning is a type of Machine Learning where a model learns from labeled data, using input features (X) and known output/target (y), to make predictions on new data.

# Main Types :

# 1. Classification → Predicts a category/class
#    Example: Spam / Not Spam

# 2. Regression → Predicts a numerical value
#    Example: House Price


# Basic Workflow :

# Labeled Data
#      ↓
# Input (X) + Output (Y)
#      ↓
# Training
#      ↓
# Model
#      ↓
# Prediction
#      ↓
# Evaluation

#                     SUPERVISED MACHINE LEARNING
#                               │
#                  ┌────────────┴────────────┐
#                  ↓                         ↓
#           CLASSIFICATION               REGRESSION
#                  │                         │
#        ┌─────────┼─────────┐       ┌───────┼────────┐
#        ↓         ↓         ↓       ↓       ↓        ↓
#    Logistic     KNN     Decision  Linear   KNN    Decision
#    Regression           Tree      Regression      Tree
#                         Classifier                 Regressoion


# Linear Regression is a supervised Machine Learning algorithm used to predict a continuous numerical value by finding a linear relationship between input features (X) and the target variable (y).

# Formula : y = mx + c

# Where:

# y = Predicted output
# x = Input feature
# m = Slope/Coefficient
# c = Intercept

# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(X , y)
# model.predict([[value]])


# CLASSIFICATION : Classification is a supervised Machine Learning technique used to predict a categorical class or label for a given input.

# Classification predicts labels while Linear regression predicts continous numerical values.
# Example of Classification : Spam or Not a Spam


#           CLASSIFICATION               
#                  │                         
#        ┌─────────┼─────────┐      
#        ↓         ↓         ↓       
#    Logistic     KNN     Decision 
#    Regression           Tree     
#                         Classifier     


# Logistic Regression : Logistic Regression is a supervised Machine Learning algorithm used for classification problems. It predicts the probability of an observation belonging to a particular class.

# Key Points
# Type: Supervised Learning
# Task: Classification
# Output: Categorical class
# Uses the Sigmoid (Logistic) function to convert predictions into probabilities.
# Probability ranges from 0 to 1. (0 ---> NO  , 1 ---> YES)
# Commonly used for binary classification.

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



# KNN (K-Nearest Neighbour) ---> KNN is a supervised Machine Learning algorithm that predicts the output of a new data point based on the K most similar/nearest data points in the training dataset.

# NOTE : KNN best works for small dataset and always assume the value of k as an odd value.

# Important Points
# Type: Supervised Learning
# Classification: Uses majority voting.
# Regression: Usually uses the average of neighboring values.
# Distance: Commonly uses Euclidean distance.
# Scaling: Important because KNN is distance-based.
# Training: KNN is called a lazy learning algorithm because it does little computation during training and performs most work during prediction.
# Scikit-learn Syntax


# STEPS : 

# 1. Choose the value of K {Odd Value}
#         ↓
# 2. Calculate the distance
#    between the new data point
#    and all training data points
#         ↓
# 3. Find the K nearest neighbors
#         ↓
# 4. Classification → Majority Voting
#    Regression → Average of values
#         ↓
# 5. Assign the final prediction



# DECISION TREE : A Decision Tree is a supervised Machine Learning algorithm that makes predictions by repeatedly splitting data based on feature values, forming a tree-like structure of decisions.

# Main Components
# Root Node → Starting point of the tree.
# Decision Node → A point where data is split based on a condition.
# Branch → Represents the outcome of a decision.
# Leaf Node → Final prediction/output.


# 1. Start with the complete dataset
#           ↓
# 2. Select the best feature for splitting
#           ↓
# 3. Split the dataset
#           ↓
# 4. Repeat the process for each branch
#           ↓
# 5. Stop when a stopping condition is reached
#           ↓
# 6. Make prediction using the leaf node


from sklearn.tree import DecisionTreeClassifier
X = [ #size , shade
    [180,7],
    [200,7.5],
    [250,8],
    [300,8.5],
    [330,9],
    [360,9.5]
]
# 0 ---> Apple  , 1 ---> Orange
y = [0,0,0,1,1,1]

model = DecisionTreeClassifier()
model.fit(X , y)

size = float(input("Enter the size in cm : "))
shade = float(input("Enter the color shade(1 - 10) : "))

result = model.predict([[size , shade]]) [0]

if result == 0:
    print("This is likely an Apple")
else :
    print("This is likely an Orange")


# Decision Tree 3 Important Points :
# 1.) Decision tree works well if it has a proper path.(e.g. just like banking loan approval).
# 2.) More the training data , more the smart the model becomes.[Leads to overfitting which is not too good.]
# 3.) Decision tree is easy to understand and explain as it has proportions.


