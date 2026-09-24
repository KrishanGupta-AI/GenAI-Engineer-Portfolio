# Function is a group of tasks performing a specific task.

# Function Call  : Whenever we want to call a function,we put the name of the function followed by parentheses as follows:
# func() #This is called the function call.

def func():
    print("Hello")
func()    

# Types of functions in python : 
# 1.)Built-in function (Already present in python).
# 2.)User defined function (Defined by the user.)

# Functions with arguments : A function can accept some values it can work with.We can put these values in the parentheses.
# A function can also return value as shown :


def avergae():
    a = int(input("Enter your number : "))
    b = int(input("Enter your number : "))
    c = int(input("Enter your number : "))

    average = (a+b+c)/3
    print("Average of your numbers is : " , average)
avergae()    

# If you want to pass name without argument function and with the help of input function.
def good_day():
    name = input("Enter your name ?")
    print("Good Day!",name)
good_day()


# If you want to use the argument function.It saves you from using the input function.
def good_day(name , ending):
    print("Good Day!",name)
    print("Thank you" , ending)
good_day("Krishan","Everyone")

#Return function ---> If we enter a value into a variable and than run that variable , no value or output will be shown except None as no value is entered to be returned.
#To get a value as output , we must enter a return value. 
def goodDay(name,ending):
    print("Good Day " + name)
    print(ending)
    return "OK"

a  = goodDay("Krishan" , "Thank You")
print(a)

#Default Argument :
def goodDay(name , ending = "Thank You"):
    print(f"Good Day , {name}")
    print(ending)

goodDay(name = "Krishan")
goodDay(name = "Akshat" , ending = "Thanks")

# Recursion ---> Recursion is a function which calls itself.It is used to directly use a mathematical formula as a function.

def factorial (n):
    if(n ==1 or n==0):
        return 1
    return n*factorial(n-1)

n = int(input("Enter a number?"))
print(f"The factorial of this number is : {factorial(n)}")



