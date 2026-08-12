# NumPy (Numerical Python) is a powerful Python library used for numerical computing and
# mathematical operations. It provides support for multi-dimensional arrays (ndarrays) and a 
# large collection of functions for performing fast and efficient mathematical computations.

# Uses of NumPy
# 1.) Creating and manipulating arrays (1D, 2D, 3D, etc.).
# 2.) Performing mathematical operations such as addition, subtraction, multiplication, and division.
# 3.) Executing statistical operations like mean, median, standard deviation, minimum, and maximum.
# 4.) Performing linear algebra operations such as matrix multiplication, transpose, and inverse.
# 5.) Generating random numbers for simulations and machine learning.
# 6.) Efficient data processing, as NumPy arrays are much faster and use less memory than Python lists.
# 7.) Serving as the foundation for libraries like Pandas, Scikit-learn, TensorFlow, and many other data science and machine learning libraries.


# An array is a collection of elements of the same data type stored in contiguous memory locations,
# where each element can be accessed using an index.
import numpy as np
#Syntax to create an array : np.array([List_of_elements])
array = np.array([1,2,3,4,6,7,89,00,0])
print(array)

# A One-Dimensional (1D) array is a collection of elements of the same data type stored in 
# a single row, where each element is accessed using a single index.
arr_1d = np.array([1,2,3,4,5,6,7,8,9,0])
print("1-Dimensional Array")
print(arr_1d)

# A Two-Dimensional (2D) array is a collection of elements of the same data type arranged in 
# rows and columns, where each element is accessed using two indices (row and column).
arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print("2-Dimensional Array")
print(arr_2d)

# A Multidimensional (nD) array is an array with two or more dimensions that stores elements
# of the same data type and is accessed using multiple indices.
multidimensional_array = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])
print("Multi-Dimensional Array")
print(multidimensional_array)

# A matrix is a two-dimensional collection of elements arranged in rows and columns,
# where each element is accessed using its row and column indices.
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Matrix")
print(matrix)


#Zeroes-Array ---> Array with all values as zero.
#np.zeros(shape)
print("Zeros Array")
print(np.zeros((3,3)))


#Ones-Array ---> Array with all values as one.
#np.ones(shape)
print("Ones Array")
print(np.ones((2,3)))


#Full Array --->Contains value of our choice.(All values are same).
#np.full(shape,value)
full_array = np.full((3,4) , 8)
print(full_array)


# The arange() function in NumPy is used to generate an array of evenly spaced numbers within a given
# range by specifying the start value, stop value, and step size.
# Syntax : np.arange(start, stop, step)
# start – Starting value (inclusive). Default is 0.
# stop – Ending value (exclusive).
# step – Difference between consecutive values. Default is 1. 
print(np.arange(1,10,1))

# An Identity Matrix is a square matrix whose diagonal elements are all 1 and
# all non-diagonal elements are 0. It is commonly represented by I.
#Syntax : np.eye(shape)
print("Identity matrix")
print(np.eye(3))

# The shape of an array is a tuple that represents the size of the array in each dimension,
# such as the number of rows and columns. It is accessed using the shape attribute in NumPy.
arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print("Shape of Array")
print(arr_2d.shape)


# The size of an array is the total number of elements it contains, regardless of its dimensions. 
# It is accessed using the size attribute in NumPy.
print("Size of Array")
print(arr_2d.size)


# ndim is a NumPy attribute that returns the number of dimensions (axes) of an array.
print("ndim of Array")
print(arr_2d.ndim)


#dtype is a NumPy attribute that returns the data type of the elements present in an array.
print("dtype of Array")
print(arr_2d.dtype)
# A NumPy array cannot store multiple data types simultaneously. If different data types are
# provided, NumPy automatically converts all elements to a common compatible data type.

# astype() is a NumPy method used to change the data type of the elements in an array by creating
# and returning a new array with the specified data type.
# SYNTAX : array_name.astype(new_data_type)
print("astype method")
print(arr_2d.astype(float))

# NumPy operators are used to perform element-wise arithmetic, comparison, logical,
# and bitwise operations on NumPy arrays.
array = np.array([1,2,3,4,5,6,7,8,9,10])
print(array + 5)   # Addition Operator
print(array - 5)   # Subtraction Operator
print(array * 5)   # Multiplication Operator
print(array / 5)   # Division Operator
print(array ** 5)  # Power(Exponent) Operator
print(array % 5)   # Modulus Operator
print(array // 5)  # Floor Division Operator


# Aggregation functions in NumPy are functions that perform calculations on multiple array elements 
# and return a single summarized value.

# Common Aggregation Functions
# Function	Description
# np.sum(array_name)	    ---->   Returns the sum of all elements
# np.mean(array_name)       ---->   Returns the average (mean) of the elements
# np.max(array_name)	    ---->   Returns the largest element
# np.min(array_name)	    ---->   Returns the smallest element
# np.median(array_name)	    ---->   Returns the median value
# np.std(array_name)        ---->	Returns the standard deviation
# np.var(array_name)	    ---->   Returns the variance
# np.prod(array_name)	    ---->   Returns the product of all elements

array_0 = np.array([10,20,30,40,50])

print("Sum of Array")
print(np.sum(array_0))

print("Mean of Array")
print(np.mean(array_0))

print("Maximum Value of Array")
print(np.max(array_0))

print("Minimum Value of Array")
print(np.min(array_0))

print("Median of Array")
print(np.median(array_0))

print("Standard Deviation of Array")
print(np.std(array_0))

print("Variance of Array")
print(np.var(array_0))

print("Product of Array")
print(np.prod(array_0))


# Indexing in NumPy is the technique of accessing one or more elements of an array using their index positions.
# SYNTAX :
# For 1-D Array : array_name[index]
# For 2-D Array : array_name[row_index, column_index]
# For 3-D Array : array_name[array_index, row_index, column_index]

array_0 = np.array([10,20,30,40,50])
print(array_0[2])

arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])
print(arr_2d[0,2])

multidimensional_array = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])
print(multidimensional_array[1,1,0])


# Slicing in NumPy is the technique of extracting a portion of an array by specifying 
# the start index, stop index, and optional step size.

# SYNTAX : array_name[start:stop:step]
# start → Starting index (inclusive)
# stop →  Ending index (exclusive)
# step →  Diffrence between elements

array_0 = np.array([10,20,30,40,50,60])
print(array_0[0:3:1])
print(array_0[::-1]) #To reverse the array

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
# For 2-D Array
# SYNTAX : array[row_slicing , column_slicing]
print(arr[0:2, 1:3])

# Fancy Indexing in NumPy is the technique of selecting one or more specific elements from an
# array using a list or NumPy array of index positions.
# SYNTAX : array_name[[index1, index2, index3]]

array_0 = np.array([10,20,30,40,50,60])
print(array_0[[0,3,5]])

# Boolean Masking in NumPy is the process of filtering or selecting array elements by applying a
# Boolean condition, where only the elements corresponding to True are returned.
# SYNTAX : array_name[condition]

print(array_0[array_0 > 30])

# Reshaping in NumPy is the process of changing the dimensions of an array while keeping the
# total number of elements the same. It is performed using the reshape() method.
# SYNTAX : array_name.reshape(new_rows, new_columns)
 
array = np.array([1,2,3,4,5,6])
print(array)
print("Reshaping of Array")
print(array.reshape(2,3))

# flatten() is a NumPy method that converts a multidimensional array into a one-dimensional
# array by returning a copy of the original array.

arr = np.array([[1, 2], [3, 4]])
new_arr = arr.flatten()
print(new_arr)


# ravel() is a NumPy method that converts a multidimensional array into a one-dimensional array
# by returning a view of the original array whenever possible.

arr = np.array([[1, 2], [3, 4]])
new_arr = arr.ravel()
print(new_arr)

# | `flatten()`                                                          | `ravel()`                                                                |
# | -------------------------------------------------------------------- | ------------------------------------------------------------------------ |
# | Returns a **copy** of the array.                                     | Returns a **view** of the original array (whenever possible).            |
# | Changes to the flattened array **do not affect** the original array. | Changes to the raveled array **may affect** the original array.          |
# | Uses more memory because it creates a copy.                          | Uses less memory because it usually shares data with the original array. |
# | Slightly slower.                                                     | Slightly faster.                                                         |


