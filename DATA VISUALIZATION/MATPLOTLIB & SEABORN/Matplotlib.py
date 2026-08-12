import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("MATPLOTLIB & SEABORN & PLOTLY/Automobile.csv")
print(df.head())

print(df.shape)

# To plot a line plot data using Matplotlib : 
# Points to be plotted : [(1, 3), (2, 5), (3, 9)]
x_value = [0,1,2]
y_value = [3,5,9]   
# plt.plot(x_value,y_value)
# print(plt.show())   

# UNIVARIATE ANALYSIS ---> Single variable analysis is called univariate analysis. 
# It is the simplest form of analyzing data. "Uni" means "one", so in this type of analysis, we only deal with one variable.
# The purpose of univariate analysis is to describe the data and find patterns that exist within it.

# Univariate analysis on categorical data : 
print(df['origin'])  # Categorical Data
print(df['origin'].unique()) # Used to find unique values in the column
categorical_counts = df['origin'].value_counts() # Used to count the number of occurrences of each unique value in the column
print(categorical_counts)

# Creation of a bar plot using Matplotlib for a Categorical Data :
# x_bar = categorical_counts.index
# y_bar = categorical_counts.values
# plt.figure(figsize = (5,5)) #Used to customize the size of figure accoriding to our choice.(ALways used before creating the chart).
# plt.xticks(rotation = 90 , fontsize = 20) #Used to rotate the xlabels(by any degree) and to change the font size as well.
# plt.bar(x_bar , y_bar , width = 0.8 , color = 'red') #Used to plot the bar chart and width is used to change its width while color is used to give desired color to the chart itself. Default width of bar chart is 1.
# plt.xlabel("Country" , fontsize = 30) #Used to give heading to the x label itself.
# plt.ylabel("Count" , fontsize = 30) #Used to give heading to the y label itself.
# plt.title("Car Production Analysis")
# plt.show()


# Creatioon of a pie chart using Matplotlib for a Categorical Data :
# Pie chart is basically used to display propotion instead of count.
# features_data = df[['displacement' , 'horsepower' , 'weight' , 'acceleration']]
# To create a pie chart we convert desired columns into rows for getting there sum , we do this by creating there transpose using functionT
# and then getting there sum by doing T.sum(axis = "columns")
# region_features = features_data.T.sum(axis = "columns")
# print(region_features)
# plt.pie(region_features , labels = region_features.index , startangle = 90 , explode = (0.2,0,0,0) , autopct = '%1.1f%%')
# region_features contains the numerical values that will be plotted as slices in the pie chart.

# labels = region_features.index
# It is used to display the names (labels) of each slice in the pie chart.
# Here, the labels are the index values of the region_features Series.

# startangle = 90
# It specifies the angle (in degrees) from which the first slice of the pie chart starts.
# A value of 90 starts the chart from the top.

# explode = (0.2, 0, 0, 0)
# It is used to separate (explode) one or more slices from the center of the pie chart.
# A larger value moves the slice farther away from the center.
# Here, only the first slice is exploded.

# autopct = '%1.1f%%'
# It is used to display the percentage of each slice on the pie chart.
# '%1.1f%%' means the percentage is displayed with one digit after the decimal point.
# Example: 25.4%

# plt.title("Features Of Cars")
# plt.show()


# print(df.describe())

# How to visualize numerical data ? 
# Histogram , Histogram shows data distribution and outliers.It is basically used to demonstrate the statistics of the data.
# Skewness refers to the asymmetry (unevenness) of a data distribution. It tells us whether the data is spread more towards the left or the right side.
# In a histogram, skewness is identified by looking at the direction of the longer tail(Very small bar chart which seems to be tail).
# The tail region often includes the outliers.
# Skewness is noise of the chart which is needed to be removed.

# If the skewness is on the left side , it is known as left skewed chart while if skewness is on right side , it is known as the right skewed chart.

# plt.hist(df["horsepower"] , bins = 5) #Bins is the number of blocks or bar chart we say.
# plt.show()

# Creation of Box plot using Matplotlib for Numerical or Numerical vs Categorical Data :

# Box plot ---> Box plot demonstrates the data distribution in a better manner.
# A Box Plot is a graphical representation of a dataset using the five-number summary.
# It works on numerical data and shows there statistics and also tells whether they contain noise(outlier) or not.

# Why do we use a Box Plot?
# A Box Plot helps us to:

# • Understand the distribution of data.
# • Find the median (middle value).
# • Measure the spread of data.
# • Compare multiple datasets.
# • Detect outliers (unusually high or low values).
# • Identify skewness in the data.


# Five-Number Summary
# A Box Plot is based on these five values:

# 1. Minimum → Smallest value (excluding outliers)
# 2. First Quartile (Q1) → 25th percentile
# 3. Median (Q2) → 50th percentile
# 4. Third Quartile (Q3) → 75th percentile
# 5. Maximum → Largest value (excluding outliers)

# Creation of a Scatter Plot using Matplotlib for Numerical - Numerical Data :

# Scatter plot basically gives a wholeistic overview which line plot can't give.
# Scatter plot helps in visualizing or depicting the correlation between two numerical variables.
# Correlation  tells us how one variable changes when another variable changes.
# When should a scatter plot be used for data analysis?
# 1.) No Time / Sequence ---> Used when data lacks a natural order , focusing on relationships between variables.
# 2.) Modeling & Prediction ---> Useful for fitting regression lines to explain variable relationships.
# 3.) Relationship Exploration ---> Ideal for visualizing correlations and detecting patterns or outliers.
# 4.) Data Distribution ---> Helps understand the spread of data and strength of association. 



# Creation of a Count Plot using Matplotlib for Categorical - Categorical Data :
# There are two types of Count Plot : 
# 1.) Stacked Countplot ---> Shows the distribution of categories within each other by stacking bars.
# 2.) Dodged Countplot  ---> Displays categories side by side , allowing for easy comparison.

# To get count of all cars.
# print(df['name'].value_counts())

# To get top 5 Count of cars
top_5_cars = df['name'].value_counts().index[:5] 
print(top_5_cars) 

top_5_mpg = df['mpg'].value_counts().index[:5]
print(top_5_mpg) 

top_5_horsepower = df['horsepower'].value_counts().index[:5] 
print(top_5_horsepower) 

top_5_weight = df['weight'].value_counts().index[:5] 
print(top_5_weight)

# top_5_data = df.loc[
#     (df['horsepower'].isin("top_5_horsepower")) |
#     (df['mpg'].isin("top_5_mpg")) |
#     (df['weight'].isin("top_5_weight")) |
#     (df['name'].isin("top_5_cars"))
# ]
# Here you're using AND (&) between all four conditions.
# This means a row must satisfy all of these simultaneously:

# Car name is in the top 5 names.
# MPG is in the top 5 most frequent MPG values.
# Horsepower is in the top 5 most frequent horsepower values.
# Weight is in the top 5 most frequent weight values.

# It is very unlikely that many (or any) rows satisfy all four conditions, so top_5_data may be empty.



# If you want rows matching any of these conditions

# Use OR (|) instead:

# top_5_data = df.loc[
#     (df['horsepower'].isin(top_5_horsepower)) |
#     (df['mpg'].isin(top_5_mpg)) |
#     (df['weight'].isin(top_5_weight)) |
#     (df['name'].isin(top_5_cars))
# ]


# Creation of Heatmap using Matplotlib for 
# A Heatmap is a graphical representation of data where values are represented using different colors. It helps visualize patterns, relationships, and the intensity of values in a dataset
# Heatmap is best used for :
# 1.) Numeric Matrix Data
# 2.) Summary Values Focus
# 3.) Correlation Analysis Best
# Why do we use a Heatmap?

# Heatmaps help us to:

# • Identify patterns in data.
# • Visualize correlations between variables.
# • Compare values across categories.
# • Detect high and low values quickly.
# • Find trends and anomalies.



# A Pair Plot is a visualization that displays pairwise relationships between multiple numerical variables in a dataset. It combines scatter plots and distribution plots into a single grid.

# print(df.columns)
# print(df.head(5))

