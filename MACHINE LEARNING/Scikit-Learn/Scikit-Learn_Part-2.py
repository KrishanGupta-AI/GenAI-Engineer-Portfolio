import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

from sklearn.linear_model import LinearRegression , LogisticRegression
from sklearn.metrics import mean_squared_error , mean_absolute_error , r2_score

# Unsupervised Learning — Unsupervised Learning is a type of machine learning where the model learns patterns, relationships, or structures from unlabeled data, without being given a target/output variable.

# Example : Grouping customers into different categories based on their purchasing behavior without knowing the categories beforehand.

# Main types of Clustering :

# 1.) Clustering → K-Means, DBSCAN, Hierarchical Clustering
# 2.) Dimensionality Reduction → PCA


# Cluster — A cluster is a group of data points that are similar to each other and different from data points in other groups.

# Example : If we have customer data, clustering might group customers into :

# Cluster 1 → Low-spending customers
# Cluster 2 → Medium-spending customers
# Cluster 3 → High-spending customers


# NOTE : Clustering is a part of Unsupervised Learning.
# NOTE : Clustering does not predicts values but group similar data points in a single group or cluster.


# Supervised Learning vs Unsupervised Learning :

# Feature	             Supervised Learning	            Unsupervised Learning
# Data	                 Labeled data	                    Unlabeled data
# Target/Output (y)      Available	                        Not available
# Goal	                 Predict the correct output	        Find hidden patterns or groups
# Learning               Learns from input-output examples	Discovers structure from input data

# SUPERVISED LEARNING :
# Input (X) + Known Output (y)
#           ↓
#         Model
#           ↓
#      Predicted Output


# UNSUPERVISED LEARNING :
# Input (X) only
#      ↓
#    Model
#      ↓
# Patterns / Groups / Structure

# Mean — Mean is the average value of a set of numbers, calculated by adding all the values and dividing the sum by the total number of values.

# Centroid — Centroid is the mean (average) position of all the data points in a cluster.
# In K-Means clustering, the centroid represents the center of a cluster.

# For a 2D Cluster :
# Centroid = (Mean of X values, Mean of Y values)

# Q-1.) Find Mean?
# A - 100
# B - 150
# C - 200
# D - 210
# E - 300

# Mean = (A+B+C+D+E)\5 = 192

# Q-2.) Find Centroid?
# Customer      Age         Spending
# A             20          100
# B             25          200
# C             30          300

# Centroid = (Mean of X value , Mean of Y value) = (25 , 200)

# Use cases in clustering
# Mean: Used to calculate the average position of data points within a cluster.
# Centroid: Used as the center/reference point of a cluster to assign new data points to the nearest cluster.

# Example: In customer clustering, the centroid represents the typical customer profile of each group. 


# Eucledian Distance : Euclidean Distance is the straight-line distance between two data points.
# In clustering, it is commonly used to measure how close a data point is to a centroid.

# Formula for 2D points : 
# Euclidean Distance = √[(X₂ - X₁)² + (Y₂ - Y₁)²]

# Euclidean Distance is used in K-means Clustering , KNN and Outliers Detection.

# Q-3.) Find Eucledian Distance ?
# Customer      Age         Spending
# A             20          100
# B             25          200

# Eucledian Distance = sqrt(20 - 25)^2 + (100 - 200)^2 = sqrt(10025) = 100.12


# Variance — Variance measures how much the data points are spread out from their mean (average).
# Variance = Σ (Value - Mean)² / Number of Values

# Low variance → Data points are close to the mean.
# High variance → Data points are widely spread from the mean.



# Spread — Spread describes how widely the data values are distributed or scattered around the mean.

# Small spread → Values are close together. [ 10, 11, 12  ] → Small spread
# Large spread → Values are far apart.      [ 10, 50, 100 ] → Large spread


# PCA — Principal Component Analysis :PCA is a dimensionality reduction technique that transforms many features into a smaller number of new features called principal components, while preserving as much important information (variance) as possible.
# In simple words : PCA reduces the number of features while keeping the most important patterns in the data.

# Example :

# 10 Features
#      ↓
#     PCA
#      ↓
# 2 Principal Components


# Main uses : 

# Reduce dimensionality
# Remove redundant information
# Visualize high-dimensional data
# Speed up machine learning models
# Reduce noise



# K-Means Clustering : K-Means Clustering is an unsupervised machine learning algorithm that divides unlabeled data into K groups (clusters) based on the similarity between data points.
# It basically assigns each data point to the nearest centroid and repeatedly updates the centroids until the clusters stabilize.

# Basic Steps of K-Means Clustering :

# Choose K
#    ↓
# Initialize K centroids
#    ↓
# Calculate distance from each point to centroids
#    ↓
# Assign points to nearest centroid
#    ↓
# Recalculate centroids using mean
#    ↓
# Repeat until centroids stop changing

# Elbow Method : The Elbow Method is a technique used in K-Means clustering to determine the optimal number of clusters (K).
# It plots the Within-Cluster Sum of Squares (WCSS) for different values of K and looks for the point where the decrease in WCSS starts becoming much smaller — this point looks like an "elbow."

# Example
# K = 1 → WCSS = 500
# K = 2 → WCSS = 300
# K = 3 → WCSS = 180
# K = 4 → WCSS = 150  ← Elbow
# K = 5 → WCSS = 140
# K = 6 → WCSS = 135

# Here, K = 4 would be a reasonable choice because after 4, the improvement becomes relatively small.

# Remember
# Elbow Method
#      ↓
# Try different K values
#      ↓
# Calculate WCSS
#      ↓
# Plot K vs WCSS
#      ↓
# Find the "Elbow"
#      ↓
# Optimal K


import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample Data
data = {
    "Customer" : ["Riya" , "Aman" , "Faizan" , "Neha" , "Imran" ,"Sneha"],
    "Age"      : [20 , 30, 40 , 22 , 38 , 25],
    "Spending" : [100 , 200 , 300 , 110 , 290 , 130]
}

df = pd.DataFrame(data)

X = df[["Age" , "Spending"]] # Feature

model = KMeans(n_clusters = 2 , random_state = 42 , n_init = 10)

# K-Means(n_clusters=2, random_state=42, n_init=10) creates a K-Means clustering model.

# n_clusters=2: Tells the model to divide the data into 2 clusters.
# random_state=42: Ensures that the random initialization produces the same results each time the code is run.
# n_init=10: Runs the K-Means algorithm 10 times with different initial centroid positions and selects the best clustering result.

# In short:
# K = 2 → Number of clusters
# random_state = 42 → Reproducible results
# n_init = 10 → Try 10 initializations and choose the best one.

df['Group'] = model.fit_predict(X)

plt.figure(figsize = (6 , 5))
for group in df['Group'].unique():
    grouped_data = df[df["Group"] == group]
    plt.scatter(grouped_data['Age'] , grouped_data['Spending'], label = f'Group{group}')

plt.xlabel("Age")
plt.ylabel("Spending Score")
plt.title("Customer Segements(K-Means)")
plt.legend()
plt.grid(True)
plt.show()    

print(df)

# df['Group'] = model.fit_predict(X) assigns each data point to a cluster and stores the cluster number in a new Group column.

# fit_predict(X) first trains the K-Means model, finds the centroids, and then assigns each data point to its nearest centroid.

# plt.figure(figsize=(6, 5)) creates a plot with a width of 6 and height of 5.

# for group in df['Group'].unique(): loops through each unique cluster number, such as 0 and 1.

# grouped_data = df[df["Group"] == group] selects only the rows that belong to the current cluster.

# plt.scatter(grouped_data['Age'], grouped_data['Spending'], label=f'Group {group}') creates a scatter plot where Age is on the X-axis and Spending is on the Y-axis, with each cluster displayed separately.


# In the Elbow Method, you usually don't choose one n_clusters value beforehand. Instead, you try a range of K values and calculate WCSS for each one.

# For example:
# wcss = []

# for k in range(1, 11):
#     model = KMeans(n_clusters=k, random_state=42, n_init=10)
#     model.fit(X)
#     wcss.append(model.inertia_)


# Principal Component Analysis (PCA) : PCA is a dimensionality reduction technique used to reduce the number of features in a dataset while retaining as much important information (variance) as possible.
# PCA is mainly used for:

# 1.) Reducing dimensions
# 2.) Visualizing high-dimensional data
# 3.) Removing redundant information
# 4.) Reducing noise
# 5.) Making models faster

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data = {
    "Age"       : [25 , 30 , 35 , 40 , 45 , 50],
    "Income"    : [30000 , 40000 , 50000 , 60000 , 70000 , 80000],
    "Spending"  : [70 , 60 , 50 , 40 , 30 , 20],
    "Savings"   : [1000 , 5000 , 8000 , 10000 , 15000 , 20000]
}

df = pd.DataFrame(data)

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

pca = PCA(n_components = 2)
pca_result = pca.fit_transform(scaled_data)

pca_df = pd.DataFrame(pca_result , columns = ["PCA1" , "PCA2"])

explained_variance = pca.explained_variance_ratio_
print("Variance Captured by each PCA Component :")
print(np.round(explained_variance * 100 , 2))

plt.figure(figsize = (8 , 6))
plt.scatter(pca_df['PCA1'] , pca_df["PCA2"] , color = "black" , s = 80)
plt.title("PCA Projection(2D View)")
plt.xlabel("PCA1 Main Pattern")
plt.ylabel("PCA2 Minor Pattern")
plt.grid(True)
plt.show()

print("New data with 2 features PCA1 and PCA2")
print(pca_df)

