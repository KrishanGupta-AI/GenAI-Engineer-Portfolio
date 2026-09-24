# 3 - Golden Rules for Data Visualiztion :

# 1.) Are X and Y numeric ?
# If Yes , create a scatter plot for there relationships.

# 2.) Is one column a category ?
# If Yes , then create a Bar Plot / Count Plot.

# 3.) Want to see a distribution ?
# Create a Histogram or KDE plot or Box plot.


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

from sklearn.linear_model import LinearRegression , LogisticRegression
from sklearn.metrics import mean_squared_error , mean_absolute_error , r2_score


data = pd.read_csv("Scikit-Learn/Student_Performance.csv")

df = pd.DataFrame(data)
print(df.head(5))

print(df.columns)

X = df[["study_hours"]]
y = df["overall_score"]

model = LinearRegression()
model.fit(X,y)

hours_studied = float(input("Enter number of hours you studied : "))

prediction = model.predict(pd.DataFrame([hours_studied] , columns = ["study_hours"])) [0]

predicted_score = model.predict(X)

print("Marks you might score based on number og hours you studied is :" , prediction)

mae = mean_absolute_error(y , predicted_score)
mse = mean_squared_error(y , predicted_score)
rmse = np.sqrt(mse)
r2 = r2_score(y , predicted_score)


print("Mean Absolute Error (MAE) is : "      , mae , round(mae,2))
print("Mean Squared Error (MSE) is : "       , mse , round(mse,2))
print("Root Mean Squared Error (RMSE) is : " , rmse , round(rmse,2))
print("R^2 Score (Model Accuracy) :" , r2 , round(r2 , 4))


# HISTOGRAM
plt.figure(figsize = (10,6))
plt.hist(data["overall_score"] , bins = 30 , color = 'skyblue' , edgecolor = 'black')
plt.title("Distribution of Overall Score")
plt.xlabel("Final Exam Score")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()


# SCATTER PLOT
plt.figure(figsize = (10,6))
plt.scatter(X, y, color = 'purple', label = "Actual Scores")


plt.plot(X , predicted_score , color = "red" , label = "Predicted Scores(Regression Line)")
plt.title("Distribution of Overall Score")
plt.xlabel("Study Hours Per Week")
plt.ylabel("Number of Students")
plt.grid(True)
plt.show()


new_hours = float(input("Enter number of hours you studied : "))
new_prediction = model.predict([[new_hours]])
print("Predicted Score : " , new_prediction)