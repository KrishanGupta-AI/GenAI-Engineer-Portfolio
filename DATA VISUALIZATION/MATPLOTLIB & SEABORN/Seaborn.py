# Seaborn is used for appealing themes and fewer lines of code.

# Seaborn internally uses matplotlib itself , but the major difference is that it creates more 
# visualized charts or more appealing we say , that too in less number of lines of code.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Used to import Seaborn Library
import seaborn as sns

df = pd.read_csv("MATPLOTLIB & SEABORN & PLOTLY/Automobile.csv")

# # Creation of a bar plot using Seaborn for a Categorical Data :
# sns.countplot(x  = "origin" , data = df , order = df["origin"].value_counts().index , color = "red") #Creates the bar plot in a aingle line of code.
# # To modify the plot simply use matplotlib
# plt.xlabel("Origin Country" , fontsize = 18)
# plt.show()


# We cannot create a pie chart using the Seaborn library itself.


# Creation of a histogram using Seaborn for showing data distribution and finding outliers :
# sns.histplot(df["horsepower"] , bins = 9)
# plt.show()

# Smoothened Curve / KDE (Kernel Density Plot) is used where we want to demonstrate distribution or density of distribution.
# It is a smoothened version of histogram.
sns.kdeplot(df["horsepower"])
plt.show()

# What type of distribution does the data follow ? 
# 1.) Right Skewed Distribution ---> Long tail extending to the right , indicating high outliers. (Positive Skewness) (Mean != Median != Mode)

# 2.) Left Skewed Distribution  ---> Long tail extending to the left , indicating low outliers. (Negative Skewness) (Mean != Median != Mode)

# 3.) Normal Distribution       ---> Symmetrical shape with average values concentrated in the middle. (Zero Skewness) (Mean == Median == Mode)



# Creation of a Bar Plot using Seaborn for showing data distribution and finding outliers in a better and easy way :
sns.boxplot(data = df) # For ful data
sns.boxplot(data = df['horsepower']) #For a specific single column
# First horizontal line is the minimum value , than 25% percentile , than the median , than te 75% percentile and at last the maximum value.
# These lines are followed up by the circles or dots representing the outliers.
plt.show()



# Creation of a line plot using Seaborn for a Numerical-Numerical Data :
sns.lineplot(data = df , x = df['horsepower'] , y = df['weight'])
# plt.show()
# To focus on a special part or get another line chart for it , simply apply limits.
plt.xlim(left = 130 , right = 165)
plt.show()
# We can plot multiple line plots on a single line plot chart.
# We can change the location of legend too.(:egend is the box which carries information regarding line , there color and what they represent).
plt.legend(loc = 'upper left')
# plt.legend(loc = (-0.5 , -0.5)) #To get legend out of the frame . Give it negative co-ordinates.




# Creation of a Scatter Plot using Seaborn for Numerical - Numerical Data :
sns.scatterplot(data = df , x = "origin" , y = "cylinders")
plt.show()

# Creation of a Count Plot using Seaborn for Numerical - Numerical Data :
# sns.countplot(data = top_5_data , x = "***" , hue = "on_which_count_is_being_done")  #Dodged countplot
# pd.crosstab(df['x_column'], df['hue_column']).plot(kind = 'bar', stacked = True)


# Creation of Heatmap using Seaborn : 
# sns.heatmap(data)
# For Correlation :
# correlation = df.corr(numeric_only=True)
# sns.heatmap(correlation , annot = True) #annot is true to show values on heatmap.


# Creation of Pair Plot using Seaborn : 
sns.pairplot(data = df)
plt.show()

# print(df.head(5))