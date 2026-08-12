import pandas as pd 

data = {
    "Name"              : ["Krishan" , None , "Kartik" , "Pushkar" , "Manan" , "Rakshit" , "Alok" , "Ayush" , "Piyush" , "Ritesh"],
    "Age"               : [23,None,56,32,45,32,56,43,22,46],
    "Salary"            : [100000000,None,234,51567,7839392,2534758,8576706,375669,364758,388594],
    "Performance Score" : [99,None,67,43,78,43,68,33,84,90]
}
df = pd.DataFrame(data)


#Handling Missing Values 
#df.fillna(value_to_use_instead_of_empty_or_null_value , inplace = True)
#If there is an null value in the row , than we use fillna() function to replace that null value
#with any other value(like mean , median) etc. and than make the changes in original dataset
#using the inplace function as True.
# print("Handling Missing Values")
df = pd.DataFrame(data)
# print(df)

#We are not using inplace as we are directly specifying or updating each column.
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["Performance Score"] = df["Performance Score"].fillna(df["Performance Score"].mean())

# print(df)


#interpolate()
#Interpolation is the method of filling null values with an estimated value. 
#It only works on numerical columns.
#Why interpolation is required : 
#1.) Preserves the data integrity
#2.) Smooth trends 
#3.) Avoid data loss

#Syntax : interpolate(method = "linear / polynomial / time and more" , axis = 0 , inplace = True)

import pandas as pd 

data_1 = {
    "Time"  : [1,2,3,4,5],
    "Value" : [10,None,30,None,50]
}

dm = pd.DataFrame(data_1)
# print("Before Interpolation")
# print(dm)


# print("After Interpolation")
dm['Value'] = dm['Value'].interpolate(method = 'linear')#we have not use axis and inplace as we have specified the column directly
# print(dm)

#When to use interpolation
# 1.) When we are working with time-series data.
# 2.) Numeric data with trends
# 3.) Prevents dropping rows.

#Disadvantages of interpolation :
# 1.) Cannot work with categorical data(name,city etc.)
# 2.) May predict a wrong estimated value.


#Sorting Data
#Sorting Data of 1-Column at a time.
#syntax : df.sort_values(by = "Column_name" , ascending = True/False , inplace = True)
#True for ascending order and False for descending order.

import pandas as pd

data_3 ={
    "Name"    : ["Krishan" , "Akshat" , "Varun" , "Karan"],
    "Age"     : [21,23,95,67],
    "Salary"  : [120000 , 23900 , 32330 , 340332]
      }

dk = pd.DataFrame(data_3)
# print("Before Sorting")
# print(dk)


# print("After Sorting")
# dk.sort_values("Age" , ascending = False , inplace = True)
# print(dk)


#sorting Data of multiple columns at a time.
#For multiple columns we have to pass a list of columns to apply sorting on and also a list
#specifying the type of sorting to be done on each column specifically in form of a list.
#In multiple sorting , always the first column is priortized and if the first column has two identical values , than the sorting is done on the basis of second column.
dk.sort_values(["Age","Salary"] , ascending = [False,True] , inplace = True)
# print(dk)


# Aggregation is the process of applying one or more functions to a collection of data to
# produce a single summarized result, such as the sum, average, count, minimum, or maximum.
#Types of Aggregation :

# 1.) Sum (sum())
# 2.) Average/Mean (mean())
# 3.) Maximum (max())
# 4.) Minimum (min())
# 5.) Count (count())
# 6.) Median (median())

data_3 ={
    "Name"    : ["Krishan" , "Akshat" , "Varun" , "Karan" , "Kartik"],
    "Age"     : [21,23,95,67,21],
    "Salary"  : [120000 , 23900 , 32330 , 340332 , 389044]
      }

dk = pd.DataFrame(data_3)

Average_salary  =dk["Salary"].mean()
# print(Average_salary)


#Grouping is the process of organizing data into categories based on one or more columns,
#allowing aggregate functions such as sum, mean, count, minimum, and maximum to be applied to each group individually.

#SYNTAX : df.groupby("Column_which_is_to_be_grouped")["Column_on_which_any_function_is_to_be_calculated"].function_to_be_done
grouped_data = dk.groupby("Age")["Salary"].sum()
# print(grouped_data)

#Grouping can be done on multiple columns at once nut the factor or function to be applied remains one.
grouped_data_1 = dk.groupby(["Age" , "Name"])["Salary"].sum()
# print(grouped_data_1)

#Some common grouping methods : 

# 1.) Sum (sum())
# 2.) Average/Mean (mean())
# 3.) Maximum (max())
# 4.) Minimum (min())
# 5.) Count (count())
# 6.) Standard Deviation (std())

# Merging is the process of joining two or more DataFrames using a common column (key) to create a 
# single DataFrame containing related data from all the DataFrames.

#SYNTAX : pd.merge(df1 , df2 , on = "Column_Name" , how = "type of join")
#df1 and df2 are the dataframe to be merged.
#on = "Column_name" , we have to enter the column name which is common in both the dataframe or on which the operation is to be executed.
#how = "type_of_join" , {inner,outer,cross,left,right}



import pandas as pd

#Customer DataFrame
df_customers = pd.DataFrame({
    "Customer_Id"   : [1,2,3],
    "Name"          : ["Krishan" , "Akshat" , "Bhavya"]
})

#Order DataFrame
df_orders = pd.DataFrame({
    "Customer_Id"   : [1,2,4],
    "Order_Amount"  : [2578 , 3789 , 839]
})

#As "Customer_Id" column is common , merging would be done on it.   


#INNER JOIN
df_merged = pd.merge(df_customers , df_orders , on = "Customer_Id" , how = "inner")
print("Inner Join")
#Inner join basically creates a dataframe , from the column specified by creating a dataframe with matching values in the specified column.
print(df_merged)


#OUTER JOIN
df_merged_1 = pd.merge(df_customers , df_orders , on = "Customer_Id" , how = "outer")
print("Outer Join")
# An Outer Join combines two DataFrames by including all rows from both DataFrames.
# Matching rows are merged, while non-matching rows are retained with missing values (NaN) in the corresponding columns.
print(df_merged_1)


#RIGHT JOIN
df_merged_2 = pd.merge(df_customers , df_orders , on = "Customer_Id" , how = "right")
print("Right Join")
# A Right Join combines two DataFrames by keeping all rows from the right DataFrame and the
# matching rows from the left DataFrame. Non-matching rows from the left DataFrame are discarded, while missing values are filled with NaN.
print(df_merged_2)


#LEFT JOIN
df_merged_3 = pd.merge(df_customers , df_orders , on = "Customer_Id" , how = "left")
print("Left Join")
# A Left Join combines two DataFrames by keeping all rows from the left DataFrame and the 
# matching rows from the right DataFrame. Non-matching rows from the right DataFrame are discarded, while missing values are filled with NaN.
print(df_merged_3)


#CROSS JOIN
#For cross join , we have to not specify the on = "Column_Name" , as cross join directly gives the cartesian product of both the dataFrames.
df_merged_4 = pd.merge(df_customers , df_orders , how = "cross")
print("Cross Join")
# A Cross Join combines two DataFrames by creating the Cartesian product of their rows, where 
# each row from the first DataFrame is paired with every row from the second DataFrame.
print(df_merged_4)



#Concatenation is the process of joining two or more DataFrames by adding rows or columns without
#requiring a common key or column. It is performed using the pd.concat() function in Pandas.

# pd.concat([dataframe_1 , dataframe_2] , axis = 0 or 1 , ignore_index = True or False)
# dataframe_1 , dataframe_2 are the dataframes to be cocatenated.
# axis = 0 , for row-wise concatenation while axis = 1 , for column-wise concatenation.
# ignore_index = True , to create a new index for the concatenated dataframe.


import pandas as pd 

#DataFrame_1
df_Region_1 = pd.DataFrame({
    "Customer_Id"  : [1,2,3,4],
    "Name"         : ["Krishan" , "Kirti" , "Ayushi" , "Anand"]
})

#DataFrame_2
df_Region_2 = pd.DataFrame({
    "Column_Id"    : [5,6],
    "Name"         : ["Shyam" , "Ram"]  
})

#Concatenation Horizontally
print("Horizontal Concatenation")
df_concat_0 = pd.concat([df_Region_1 , df_Region_2] , axis = 0 , ignore_index = True)
print(df_concat_0)


#Concatenation Horizontally
print("Vertical Concatenation")
df_concat_1 = pd.concat([df_Region_1 , df_Region_2] , axis = 1 , ignore_index = True)
print(df_concat_1)