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
