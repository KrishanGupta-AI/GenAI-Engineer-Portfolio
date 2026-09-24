#VARIABLES AND DATA TYPES 

# A variable is the name given to a memory location in a program.
# variable ---> container to store a value.
# keywords ---> reserved words in python.
# identifiers ---> class/function/variable name 

#DATA TYPES ----> 
# 1.) Integers (1,2,3,4,5,6,7,8,9,0)
# 2.) Floating Point Numers (1.0,2.34,56.77)
# 3.) Strings ("Krishan","Henry")
# 4.) Booleans (True , False)
# 5.) None

#Rules for defining a variable name :
# 1.) A variable name can contain alphabets , digits and underscore.
# 2.) A variable name can only start with an alphabet and underscores.
# 3.) A variable name can't start with a digit.
# 4.) No while space is allowed to be used inside a variable name.

#Operators in Python : 
# 1.) Arithmetic Operator (+ , - , * , /)
# 2.) Assignment Operator (=,+=,-=)
# 3.) Comparison Operator (==,>=,<=,>,<,!=)
# 4.) Logical Operators (and,or,not)

# or ---> Any one condition should satisfy to be true.
# and ---> Both the condition should satisfy to be true.

a = 3.4
print(type(a))

b = str(a)
print(type(b))

c = int(input("Enter a number :"))
d = int(input("Enter a number :"))
print("Sum of both numbers is " , c+d)
