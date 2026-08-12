import pandas as pd
pd.DataFrame()

#A Series is a one-dimensional labelled array that can hold any data type : integers , floats , strings ,
#or even Python objects.Each element in the series has a unique label called an index.
#It is often used to track changes or patterns over time,such as daily tempratures ,stock prices,or sales revenue.

#A DataFrame is a two-dimensional labeled data structure in pandas , similar to table in a database , an Excel spreadsheet , or a SQL table.

#It consists of rows and columns , where :
#a.) Rows have Indices(Labels).
#b.) Columns have names(Labels).

#Reading data from different files into a DataFrame
#1.) pd.read_csv("")
#2.) pd.read_excel("")
#3.) pd.read_json"") and many more....



# Read data from CSV file into a DataFrame
df = pd.read_csv("Basics_of_Pandas/data.csv")
# print(df)      



#To save file after manipulation
data = {"Name" : ["Krishan" , "Kirti" , "Ayushi"],
        "Age"  : [21,23,26],
        "City" : ["Greater Noida" , "Delhi" , "Moga"]  }

dk = pd.DataFrame(data)
print(dk)

dk.to_csv("output.csv" , index = False) 
#To save the file after manipulation as the file name "output.csv"
#Can save in any format like json , By using : dk.to_json("****.json")
#Index = False is used to not show any indexes or serial numbers in the output file as shown in normal files(E.g. --> S.no.)

#Why do we need to explore data?
#1.) To understand the dataset.
#2.) To identify the problems.
#3.) Used for planning further steps.

#head() and tail()
#head() ---> Used to display the beginning rows of the dataset.
#tail() ---> Used to display the ending rows of the dataset.

#To display starting and ending rows of the dataset.
dl = pd.read_csv("Basics_of_Pandas/data.csv")

print("Display first 5 rows of the dataset.")
# print(dl.head(5)) #Beginning 5 rows 

print("Display ending 5 rows of the dataset.")
# print(dl.tail(5)) #Ending 5 rows



#info() function is used to get an overview of the whole dataset : number of rows it has, number of columns it has ,
#whether it contains a non-null values or not, Type of data-type it contains, amount of memory it occupies.
#Types of data-types and what they represent :
#int64 ---> Represents integers.
#float64 ---> Represents decimal values.
#object ---> Represents it contains string or any categorical data. 


#Use of describe() function ---> gives information of mean of each column , there standard deviation(range that how much the value varies from the average/mean value) , minimum value , there top 25%,50% and 75% values and also the max values.
#small standard deviation means consistant data.
#min values means the minimum or least value in the each column.
#25% means if we arrange the data in a sorted manner and take the first quarter or the top 25% values , then all values would be less than the 25%value.
#50% means if we arrange the data in a sorted manner and take the first half or the top 50% values , then all values would be less than the 50%value.
#75% means if we arrange the data in a sorted manner and take the first three quarters or the top 75% values , then all values would be less than the 75%value.
#max values means the maximum or highest value in the each column.

data = {
    "Name"              : ["Krishan" , "Akshat" , "Kartik" , "Pushkar" , "Manan" , "Rakshit" , "Alok" , "Ayush" , "Piyush" , "Ritesh"],
    "Age"               : [23,24,56,32,45,32,56,43,22,46],
    "Salary"            : [100000000,234567,234,51567,7839392,2534758,8576706,375669,364758,388594],
    "Performance Score" : [99,34,67,43,78,43,68,33,84,90]
}

dh = pd.DataFrame(data)
# print(dh)

# print(dh.describe())

#Use of shape and columns function.
#shape ---> It is an attribute which returns a tuple with two values(number of rows , number of columns).
#columns ---> It is used to get the name of all the columns present in the dataset.

print(dh.shape)
print(dh.columns)


#To select a desired column or row and apply a condition on it.
#We can do this by :
#1.) By selecting the specific column.
#2.) By filtering the rows by applying the condition.
#3.) We can also combine multiple conditions to do so.

#To select columns : We use , square brackets
#To select rows : We use , boolean conditions

#Selecting columns , We get:
#A series
#DataFrame multiple columns of data.
# desired_column = df["Column_name"]
# multiple_desired_column = df["Column_name_1" , "Column_name_2"]


#Filtering Rows , We get:
#Boolean Indexing

#Based on a single condition 
#filtered_rows = df[df["Salary"] > 50000]
#multiple_conditions = df[(df["Salary"] > 50000) & (df["Column_2"] < 800000) & (df["Column_3"] == "Krishan")]
# & ---> Used when we want both the conditions to be True.
# | ---> Used when we want any one of the condition to be True.

# print(dh)

#To access a single column 
name = dh["Name"]
print("To access a single column")
print(name)

#To access multiple columns at once
subset = dh[["Name","Age","Salary"]]
print("To access multiple columns at once")
print(subset)


#To access a row applying a single condition 
condition_1 = dh[dh["Salary"] > 500000]
print("Employees with salary more than 500000")
print(condition_1)

#To access a row applying multiple conditions 
condition_2 = dh[(dh["Salary"] > 500000) & (dh["Name"] == "Krishan")]
print("Employee with salary more than 500000 and name as : Krishan")
print(condition_2)

condition_3 = dh[(dh["Salary"] > 500000) | (dh["Name"] == "Kartik")]
print("Employee with salary more than 500000 or name as : Kartik")
print(condition_3)


