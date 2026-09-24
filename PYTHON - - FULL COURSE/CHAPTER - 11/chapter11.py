# ==========================================================
# INHERITANCE IN PYTHON
# ==========================================================

# Inheritance is a way of creating a new class from an existing class.
# It helps us reuse code instead of writing everything again.

# Types of Inheritance:
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multi-Level Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


# ==========================================================
# MULTIPLE INHERITANCE
# ==========================================================

class Employee:

    # Class attribute
    company = "ITC"

    # Method of Employee class
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")


class Coder:

    # Class attribute
    language = "Python"

    # Method of Coder class
    def printLanguage(self):
        print(f"Out of all languages, here is your preferred language: {self.language}")


# Programmer inherits from BOTH Employee and Coder
# Therefore it can use methods and attributes from both classes.
class Programmer(Employee, Coder):

    company = "ITC Infotech"
    name = "Krishan"
    salary = 23939393

    def showLanguage(self):
        print(f"My name is {self.name}.")
        print(f"I work with {self.language}.")
        print(f"I work at {self.company}.")


# Creating an object
b = Programmer()

# Calling methods inherited from Employee and Coder
b.show()
b.printLanguage()
b.showLanguage()


# ==========================================================
# MULTI-LEVEL INHERITANCE
# ==========================================================

# Grandparent Class
class Krishan:

    def __init__(self):
        print("Constructor of Krishan")

    a = 1


# Parent Class
class Akshat(Krishan):

    def __init__(self):
        # Calling constructor of parent class
        super().__init__()

        print("Constructor of Akshat")

    b = 2


# Child Class
class Kartik(Akshat):

    def __init__(self):

        # Calls constructor of Akshat
        # Akshat then calls constructor of Krishan
        super().__init__()

        print("Constructor of Kartik")

    c = 3


# Creating object
o = Kartik()

print(o.a, o.b, o.c)


# Output:
# Constructor of Krishan
# Constructor of Akshat
# Constructor of Kartik
# 1 2 3


# ==========================================================
# SUPER() METHOD
# ==========================================================

# super() is used to access methods or constructors
# of the parent class.

# It helps avoid writing the parent class name directly.

# Example:
#
# super().__init__()
#
# This calls the constructor of the parent class.


# ==========================================================
# CLASS METHOD
# ==========================================================

class Manan:

    a = 1

    # Class Method
    # It works with class attributes instead of object attributes.
    @classmethod
    def show(cls):
        print(f"The class attribute 'a' is: {cls.a}")


m = Manan()

# This creates an object attribute.
m.a = 2344

# Still prints class attribute because cls refers to the class.
m.show()

# Output:
# The class attribute 'a' is: 1


# ==========================================================
# DIFFERENCE BETWEEN self AND cls
# ==========================================================

# self
# ----
# Refers to the current object.

# cls
# ---
# Refers to the class itself.

# self -> Object
# cls  -> Class


# ==========================================================
# PROPERTY DECORATOR
# ==========================================================

class Pushkar:

    # Getter Method
    # Allows us to use name like an attribute.
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    # Setter Method
    # Runs automatically when assigning a value to name.
    @name.setter
    def name(self, value):

        # Split full name into first and last name.
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


k = Pushkar()

# Calls setter automatically
k.name = "Krishan Gupta"

print(k.fname)
print(k.lname)

# Calls getter automatically
print(k.name)


# ==========================================================
# PROPERTY DECORATOR EXPLANATION
# ==========================================================

# Without @property
#
# obj.getName()
#
# With @property
#
# obj.name
#
# It behaves like a normal variable even though
# a method is running behind the scenes.


# ==========================================================
# OPERATOR OVERLOADING
# ==========================================================

# Python allows operators to behave differently for objects.
# This is called Operator Overloading.

# It is achieved using Dunder (Magic) Methods.

# Example:
#
# +  ---> __add__()
# -  ---> __sub__()
# *  ---> __mul__()
# /  ---> __truediv__()
# == ---> __eq__()
# >  ---> __gt__()
# <  ---> __lt__()

# Example:

class Number:

    def __init__(self, n):
        self.n = n

    # Overloading +
    def __add__(self, other):
        return self.n + other.n


a = Number(10)
b = Number(20)

print(a + b)

# Output:
# 30


# ==========================================================
# EASY REVISION NOTES
# ==========================================================

# 1. Inheritance
# Allows one class to use properties and methods
# of another class.

# Parent Class
# ↓
# Child Class

# Child gets all accessible features of Parent.


# 2. Types of Inheritance

# Single
# Parent → Child

# Multiple
# Parent1 + Parent2 → Child

# Multi-Level
# Grandparent → Parent → Child

# Hierarchical
# One Parent → Multiple Children

# Hybrid
# Combination of different inheritance types.


# 3. super()

# Used to call methods or constructors
# of the parent class.

# Example:
#
# super().__init__()


# 4. @classmethod

# Uses cls instead of self.
# Works with class attributes.

# Syntax:
#
# @classmethod
# def method(cls):


# 5. @property

# Converts a method into an attribute.

# Instead of:
#
# obj.getName()
#
# We can write:
#
# obj.name


# 6. @name.setter

# Runs automatically whenever
# we assign a value.

# Example:
#
# obj.name = "Krishan Gupta"


# 7. Operator Overloading

# Changes the behavior of operators
# for user-defined objects.

# Done using Dunder Methods.

# Example:
#
# __add__()
# __sub__()
# __mul__()
# __eq__()


# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

# Q1. What is Inheritance?
#
# Inheritance is the process of creating a new class
# from an existing class so that code can be reused.

# Q2. Why is Inheritance used?
#
# To reuse code, reduce duplication, and make programs
# easier to maintain.

# Q3. What is super()?
#
# super() is used to call methods or constructors
# of the parent class.

# Q4. Difference between self and cls?
#
# self -> Refers to the current object.
#
# cls -> Refers to the class itself.

# Q5. What is @property?
#
# It allows a method to be accessed like an attribute.

# Q6. What is Operator Overloading?
#
# It allows Python operators to work with user-defined
# objects using dunder methods.


# ==========================================================
# MEMORY TRICK
# ==========================================================

# Inheritance  -> Reuse code
# Parent       -> Gives properties
# Child        -> Receives properties
# super()      -> Call parent
# self         -> Current object
# cls          -> Current class
# @classmethod -> Works with class
# @property    -> Method behaves like variable
# Setter        -> Changes value
# Getter        -> Returns value
# __add__()    -> Overloads +
# ==========================================================