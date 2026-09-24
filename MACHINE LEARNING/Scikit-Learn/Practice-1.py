# Practical Aspects of Machine Learning :
# 1.) Tabular Data
# 2.) Data Prepration
# 3.) Data Evaluation
# 4.) Executable Python Code

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

data = pd.read_csv("Scikit-Learn/Practice-1.csv")

df = pd.DataFrame(data)

print(df)

X = df[["Hours"]]  # Input
y = df['Score']    # Output

model = LinearRegression()

model.fit(X, y)

hours_studied = float(input("Enter how many hours did you study: "))

result = model.predict(pd.DataFrame([[hours_studied]], columns=["Hours"]))[0]

print("Marks you might score based on the number of hours you studied:",result)

predicted_score_1  =model.predict(X)

mae = mean_absolute_error(y , predicted_score_1)
mse = mean_squared_error(y , predicted_score_1)
rmse = np.sqrt(mse)



print("Mean Absolute Error (MAE) is : "      , mae)
print("Mean Squared Error (MSE) is : "       , mse)
print("Root Mean Squared Error (RMSE) is : " , rmse)


new_hour = float(input("Enter a hour : "))
new_pred = model.predict(pd.DataFrame([[new_hour]] , columns = ["Hours"]))[0]
print(f"Prediction for {new_hour} is score = {new_pred}")


new_precition = model.predict([[7]])
print(f"Predicted Score for 7 Hour is : {new_precition}")