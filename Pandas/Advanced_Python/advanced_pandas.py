import pandas as pd 

data = {
    "Name"              : ["Krishan" , None , "Kartik" , "Pushkar" , "Manan" , "Rakshit" , "Alok" , "Ayush" , "Piyush" , "Ritesh"],
    "Age"               : [23,None,56,32,45,32,56,43,22,46],
    "Salary"            : [100000000,None,234,51567,7839392,2534758,8576706,375669,364758,388594],
    "Performance Score" : [99,None,67,43,78,43,68,33,84,90]
}
df = pd.DataFrame(data)
print("Normal Dataset")
print(df)

#Adding columns in a dataset
# df["New_Column_name"] = Values to be inserted in the column
#This method is used to add the new column at the end of the dataset.
print("Addition of a new column named : Bonus")
df["Bonus"] = df["Salary"] * 0.1
print(df) #New column will be already added in the DataFrame.


# To add the column at our desired location , we use insert() function. 
#df.insert(loc,"New_Column_name",Data)
print("Addition of a new column named : Employee_id , but on desired location.")
df.insert(2,"Employee_id",[11,12,13,14,15,16,17,18,19,20])
print(df)

#To update value of a row in a dataset
# df.loc[row_index,"Column_name"] = new_value
print("Update a particular value in Salary column by .loc() function.")
df.loc[1,"Salary"] = 56788383
print(df)

#To update values of a whole column
#df["Column_name"] = df["Column_name"]  * operation // New value
print("Used to update the values of the whole column.")
df["Salary"] = df["Salary"] *2
print(df)

#Removing columns keep your data clean and focused.
# df.drop(columns = ["Columns_name"] , inplace = True)
print("Used to delete a whole column at once.")
df.drop(columns = ["Bonus"] , inplace = True)
#inplace = True , it means that it will update this step in the original dataset.{If inplace = False , it returns a new dataset instead of updating the original dataset.} 
print(df)



#Missing Values in Pandas
#Types of missing values :
#1.) NaN ---> Not a Number
#2.) None ---> for object data types

#isnull() ---> This function is used to find that whether there is a null value present or not.
#If the solution is :
#Yes ---> NaN is missing
#No  ---> Value is present

#To find that whether there are null values present or not?
print(df.isnull())

#To find the sum/number of occurence of null values in each row.
print(df.isnull().sum())



#Handling Missing Values
#To handle missing values , we can either remove the missing values or update them with the new value.

#Removing the missing value.
# df.dropna(axis = 0 , inlace = True)
#If there is even a single missing value in the entire row , it will wipe out the entire row itself. 
#axis = 0 , Removes missing values from row while axis = 1 means column missing values.
#inplace = True means that the changes would be made in the original dataset itself.
# df.dropna(axis = 0 , inplace = True)
print(df)



#Handling Missing Values 
#df.fillna(value_to_use_instead_of_empty_or_null_value , inplace = True)
#If there is an null value in the row , than we use fillna() function to replace that null value
#with any other value(like mean , median) etc. and than make the changes in original dataset
#using the inplace function as True.
print("Handling Missing Values")
dm = pd.DataFrame(data)
print(dm)

dm.fillna(0, inplace = True)
print(dm)