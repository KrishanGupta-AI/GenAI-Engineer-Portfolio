import numpy as np

# Array modification in NumPy is the process of changing the values or structure of an array
# by updating, inserting, deleting, or appending elements.
 
# Inserting an Element in an Array
# Inserting elements in NumPy is the process of adding one or more elements to a specified position in an array using the np.insert() function.
# SYNTAX : np.insert(array , index , value , axis = row/column)
arr = np.array([10, 20, 30])
new_arr = np.insert(arr, 1, 15 , axis = 0 )
print("Inserting an Element in an Array.")
print(new_arr)

# For 2-D Array
arr_2d = np.array([
    [1, 2],
    [5, 6]
])

new_arr = np.insert(arr_2d, 1, [3, 4], axis=0)
print(new_arr)


# Appending in NumPy is the process of adding one or more elements to the end of an array using the np.append() function.
# SYNTAX : np.append(array, values, axis=None)
# array → The original NumPy array.
# values → The element(s) to append.
# axis → Specifies the axis along which values are appended (used for multidimensional arrays). The default is None.
arr = np.array([10,20,30,40])
print(np.append(arr , [40,50,60]))


# Concatenation in NumPy is the process of combining two or more arrays along a specified axis using the np.concatenate() function.
# SYNTAX : np.concatenate((array1, array2), axis=0)

# array1, array2 → Arrays to be joined.
# axis → Specifies the axis along which the arrays are joined.
# axis=0 → Join by rows (vertical concatenation).
# axis=1 → Join by columns (horizontal concatenation).  

arr_1 = np.array([1,2,3,4,5])
arr_2 = np.array([6,7,8,9,10])
new_arr = np.concatenate((arr_1 , arr_2))
print(new_arr)


# Removing elements in NumPy is the process of deleting one or more elements from an array using the np.delete() function.
# SYNTAX : np.delete(array, index, axis=None)

# array → The original NumPy array.
# index → The index (or indices) of the element(s) to remove.
# axis → Specifies the axis along which to delete.
# axis=0 → Delete row(s).
# axis=1 → Delete column(s).
# axis=None (default) → The array is flattened before deletion.

arr = np.array([10, 20, 30, 40])
new_arr = np.delete(arr, 2)
print(new_arr)


arr_1 = np.array([1,2,3,4])
arr_2 = np.array([6,7,8,9])
# Stacking in NumPy is the process of combining two or more arrays along a new axis using functions like np.vstack(), np.hstack(), and np.stack().

# Types of Stacking
# 1. Vertical Stacking (np.vstack())
# Combines arrays row-wise (one below another).
# Syntax : np.vstack((array1, array2))
print(np.vstack((arr_1,arr_2)))


# 2. Horizontal Stacking (np.hstack())
# Combines arrays column-wise (side by side).
# Syntax : np.hstack((array1, array2))
print(np.hstack((arr_1,arr_2)))


# General Stacking (np.stack())
# Joins arrays along a new axis.
# Syntax : np.stack((array1, array2), axis=0)
# np.stack() creates a new dimension, whereas vstack() and hstack() combine arrays along existing dimensions.
print(np.stack((arr_1,arr_2)))


# Splitting in NumPy is the process of dividing an array into multiple smaller arrays using functions such as np.split(), np.hsplit(), and np.vsplit().

# Types of Splitting
# np.split()
# Splits an array into equal parts along a specified axis.
# SYNTAX : np.split(array, sections, axis=0)

arr = np.array([10, 20, 30, 40])
result = np.split(arr, 2)
print(result)

# np.hsplit() (Horizontal Split)
# Splits a 2D array column-wise.
# SYNTAX : np.hsplit(array, sections)

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])
result = np.hsplit(arr, 2)
print(result)

# np.vsplit() (Vertical Split)
# Splits a 2D array row-wise.
# SYNTAX : np.vsplit(array, sections)

arr = np.array([[1, 2],
                [3, 4],
                [5, 6],
                [7, 8]])
result = np.vsplit(arr, 2)
print(result)


# Broadcasting in NumPy is the automatic expansion of smaller arrays to match the shape of larger
# arrays so that element-wise operations can be performed efficiently.

# Why is Broadcasting Used?
# 1.) To perform operations on arrays of different shapes.
# 2.) To avoid writing loops.
# 3.) To improve performance and memory efficiency.

prices = np.array([100,200,300])
discount = 10

final_price = prices - (prices * discount/100)
print(final_price)

# Broadcasting enables element-wise operations on arrays of different shapes.
# NumPy does not physically duplicate the smaller array; it logically expands it, making broadcasting memory-efficient.
# Broadcasting works when the dimensions are equal or one of them is 1.  <---- VERY IMPORTANT


# Vectorization in NumPy is the technique of performing operations on entire arrays instead of 
# individual elements using loops, resulting in faster and more efficient computation.

arr1 = np.array([10, 20, 30])
arr2 = np.array([1, 2, 3])
print(arr1 + arr2)



# Missing values in NumPy are unavailable or undefined data values, typically represented 
# by np.nan, and can be identified and handled using NumPy functions.

# np.nan is a special value in NumPy that represents missing or undefined numerical data.
arr = np.array([10, 20, np.nan, 40, 50])
print(arr)


# np.isnan() is a NumPy function used to check whether the elements in an array are missing values (np.nan). It returns a Boolean array where:
# True → The element is np.nan.
# False → The element is not np.nan.
# SYNTAX : np.isnan(array)
print(np.isnan(arr))



# np.nan_to_num() is a NumPy function that replaces np.nan, positive infinity (inf), 
# and negative infinity (-inf) with specified numerical values.
# SYNTAX : np.nan_to_num(array, nan=0.0, posinf=None, neginf=None)

# array  → Input NumPy array.
# nan    → Value to replace np.nan (default is 0.0).
# posinf → Value to replace positive infinity (inf).
# neginf → Value to replace negative infinity (-inf).

arr = np.array([10, np.nan, np.inf, -np.inf])
new_arr = np.nan_to_num(arr, nan=0, posinf=999, neginf=-12)
print(new_arr)


