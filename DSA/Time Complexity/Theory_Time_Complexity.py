# Techniques to Measure Time Complexity --->

# 1.) Measuring time to execute.
# 2.) Counting operations involved.
# 3.) Abstract notion of order of growth.


# Measuring Time --->  #Not used in industry due to different processors or hardware in each system.

import time 
start = time.time()
for i in range(1,101):
    print(i)
print("Time required to execute the problem was : ",(time.time() - start))  


# Counting Operations ---> Not used significantly.
def c_to_f(c):
    return c*9.0/5 + 32 # Has 3 operations(* , / , +)

def mysum(x):
    total = 0  # Has 1 operation (=)
    for i in range(x+1): # Has 1 operation
        total += i # Has 2 operations ( + , =)
    return total
# Total operations = 4

# So , this is not a good solution as we don't know what to take as operation and even a sinle step can change the whole 
# scenario and time complexity.Thus,it is not a very good method of time measurement.


# Orders of Growth ---> 
# # Goals : 
# 1.) We want to check how efficient a program is when the input size is very large.
# 2.) We want to understand how the program's running time increases as the input size increases.
# 3.) We want to find an upper bound for the program's growth, and we want this bound to be as tight as possible.
# 4.) We don't need the exact running time.We only care about the general order of growth, not the exact time.
# 5.) We focus on the biggest factors affecting the running time.In other words, we identify which part of the program takes the most time.
# 6.) Therefore, we generally want to find a tight upper bound for the program's growth based on the input size, especially in the worst case.

# Order of Growth is always among the following : 
# Linear , Quadratic , Constant , Logarithmic , Exponential , nlogn
# Big-O Time Complexities
# O(1) → Constant Relation
# O(log n) → Logarithmic Relation
# O(n) → Linear Relation
# O(n log n) → Linearithmic Relation
# O(n²) → Quadratic Relation
# O(2ⁿ) → Exponential Relation

# X-axis represents input
# Y-axis represents time taken by the program.

def factor(n):
    answer = 1 # 1 operation
    while n > 1: # 1 operation
        answer *= n # 2 operation
        n -= 1 # 2 operation
    return answer     # 1 operation 

# Total Operations = 1 + 5n (5n <-- Number of operations inside the loop) , (1 <-- Number of operations outside the loop.)
# Time complexity is removal of additive operations and than removal of mutiplicative number.
# Final time complexity = O(n)


# Q-1.) n^2 + 2n + 2 ---> n^2 ---> means it is a nested loop , 2n ---> means that it has 2 operations inside the loop , 2 ---> means it has 2 operations outside the loop.
# Time Complexity = O(n^2) , as 2 is already removed as additive operations are removed earlier , 2 from 2n is removed as multiplicative operations are also removed.
# Only n^2 + n is left and according to the rule of order of growth , only the biggest one is taken in consideration.
# Thus , Time Complexity is O(n^2)


# Q-2.) n^2 + 100000n + 3^1000
# Answer : O(n^2)

# Q-3.) log(n) + n + 4
# Answer : O(n) , as log(n) < n

# Q-4.) 0.0001*n*log(n) + 300n
# Answer : O(nlog(n))

# Q-5.) 2n^30 + 3^n
# Answer : O(3^n) , n^30 > 3^n

 



# O(1) ---> Constant relation , does not depend on the number of elements.
# For e.g.: Taking out first biscuit from a pack of 50 or 100.The time complexity remains same.

marks = [88 , 72 , 95 , 61 , 79]
first_marks = marks[0]
print(first_marks) # Time complexity is O(1) as the operation is not affected by the length of array.



# O(logn)  ----> Logarithmic Relation , 

def find_names(names , target):
    left = 0
    right = len(names) - 1 

    while left <= right: 
        middle = (left + right) // 2

        if names[middle] == target :
            return middle

        elif names[middle] < target:
            left = middle + 1 

        else:
            right = middle - 1

    return  -1
names = ["Aayush" , "Akshat" , "Diya" , "Krishna" , "Krishan" , "Sneha" , "Uday" , "Zara"]   
target_name = "Sneha"
result = find_names(names , target_name)

if result != -1:
    print("Found at index " , result)
else : 
    print("Sorry!Not Found")    

# Binary Search Code Explanation : 
# Define the function:

# def find_names(names, target):

# The function takes two inputs:

# names = sorted list of names
# target = name we want to find
# Set the starting and ending positions:
# left = 0
# right = len(names) - 1
# left points to the first element.
# right points to the last element.
# Start the loop:
# while left <= right:

# The loop continues as long as there are elements left to search.

# Find the middle position:
# middle = (left + right) // 2

# The middle index is calculated by taking the average of left and right.

# Check the middle element:
# if names[middle] == target:
# return middle

# If the middle name is equal to the target, return its index.

# If the middle name comes before the target:
# elif names[middle] < target:
# left = middle + 1

# Because the list is sorted, we ignore the left half and search the right half.

# If the middle name comes after the target:
# else:
# right = middle - 1

# We ignore the right half and search the left half.

# If the target is not found:
# return -1

# -1 means the name does not exist in the list.

# Example:

# names = ["Aayush", "Akshat", "Diya", "Krishna", "Krishan", "Sneha", "Uday", "Zara"]

# target = "Sneha"

# First middle:
# middle = 3
# names[3] = "Krishna"

# "Krishna" comes before "Sneha", so search the right half.

# New middle:
# middle = 5
# names[5] = "Sneha"

# Target found at index 5.

# Output:
# Found at index 5

# Main concept:

# Binary Search checks the middle element and eliminates half of the search space after every comparison.

# Time Complexity:
# O(log n) → Logarithmic Relation

# Important:
# Binary Search works correctly only when the data is sorted
          


