# ==========================================================
# OOPS in Python - Class, Object, Attributes, Self, Constructor
# ==========================================================

# A Class is a blueprint (template) used to create objects.
# Think of it like the blueprint of a house.
# Objects are the actual houses built using that blueprint.

class Employee:

    # -------------------------
    # Class Attributes
    # -------------------------
    # These belong to the class itself.
    # They are shared by all objects unless an object has its own value.
    language = "Python"
    salary = 120000
    name = "Krishan"


# ==========================================================
# Creating Objects
# ==========================================================

Harry = Employee()

# Instance/Object Attribute
# This belongs only to Harry.
Harry.residence = "Delhi"

print(Harry.name, Harry.language, Harry.salary, Harry.residence)


Akshat = Employee()

# Object attribute
Akshat.residence = "Noida"

# This creates an object attribute named 'name'
# It overrides the class attribute only for Akshat.
Akshat.name = "Akshat"

print(Akshat.name, Akshat.language, Akshat.salary, Akshat.residence)


# ==========================================================
# Quick Revision
# ==========================================================

# Class Attribute:
# - Declared inside the class.
# - Shared by every object.
# - Stored only once in the class.

# Object (Instance) Attribute:
# - Belongs to one specific object.
# - Different objects can have different values.

# If both class and object have an attribute with the same name,
# Python always gives preference to the object attribute.

# Example:
# Employee.name = "Krishan"
# Akshat.name = "Akshat"
# print(Akshat.name)   -> Akshat
# print(Harry.name)    -> Krishan


# ==========================================================
# SELF PARAMETER, CONSTRUCTOR & STATIC METHOD
# ==========================================================

class Boss:

    # Default class attributes
    language = "Python"
    salary = 120000

    # --------------------------------------------------
    # Constructor (__init__)
    # --------------------------------------------------
    # This is called automatically whenever a new object
    # is created.
    #
    # It is also known as a Dunder Method because it has
    # double underscores before and after its name.
    def __init__(self, language, salary):

        # 'self' refers to the current object.
        # These become object attributes.
        self.language = language
        self.salary = salary

    # --------------------------------------------------
    # Instance Method
    # --------------------------------------------------
    # Every instance method must have 'self' as its first parameter.
    # It allows the method to access the object's own data.
    def getInfo(self):
        print(f"My salary is {self.salary} and the language I prefer is {self.language}")

    # --------------------------------------------------
    # Static Method
    # --------------------------------------------------
    # A static method does not need 'self' because it
    # doesn't use any object data.
    @staticmethod
    def greet():
        print("Good Morning")


# ==========================================================
# Creating Objects
# ==========================================================

Harry = Boss("Python", 120000)

Harry.getInfo()

# Python internally converts:
# Harry.getInfo()
#
# into:
#
# Boss.getInfo(Harry)

Harry.greet()

Krishan = Boss("Hindi", 2300000)

Krishan.getInfo()


# ==========================================================
# EASY REVISION NOTES
# ==========================================================

# 1. CLASS
# A blueprint/template used to create objects.

# 2. OBJECT
# An instance of a class.

# Example:
# obj = Employee()

# 3. CLASS ATTRIBUTE
# Belongs to the class.
# Shared among all objects.

# Example:
# language = "Python"

# 4. INSTANCE / OBJECT ATTRIBUTE
# Belongs only to one object.

# Example:
# Harry.residence = "Delhi"

# 5. OBJECT ATTRIBUTE vs CLASS ATTRIBUTE
# If both exist with the same name,
# Python first checks the object attribute.
# If not found, it checks the class attribute.

# Therefore:
# Object Attribute > Class Attribute

# 6. SELF
# 'self' is a reference to the current object.
# It allows each object to access its own attributes and methods.

# Example:
# Harry.getInfo()
#
# Internally becomes:
#
# Boss.getInfo(Harry)

# 7. CONSTRUCTOR (__init__)
# Automatically called when an object is created.
# Used to initialize object attributes.

# Example:
# obj = Boss("Python", 120000)

# Internally:
# Boss.__init__(obj, "Python", 120000)

# 8. STATIC METHOD
# Doesn't use 'self'.
# Doesn't access object attributes.
# Behaves like a normal function kept inside the class.

# Example:
# Boss.greet()
# Harry.greet()

# Both are valid.


# ==========================================================
# Interview Questions
# ==========================================================

# Q1. What is a Class?
# A class is a blueprint used to create objects.

# Q2. What is an Object?
# An object is an instance of a class.

# Q3. Difference between Class Attribute and Object Attribute?
#
# Class Attribute:
# - Shared by all objects.
#
# Object Attribute:
# - Belongs to only one object.
#
# Object attributes always get preference over class attributes.

# Q4. What is 'self'?
#
# 'self' is a reference to the current object.
# It allows Python to know which object's attributes or methods
# should be accessed.

# Q5. What is __init__()?
#
# It is the constructor.
# It is automatically called whenever a new object is created.
# Used to initialize object attributes.

# Q6. What is @staticmethod?
#
# It creates a method that does not require 'self'.
# It is used when the method doesn't need object data.

# ==========================================================
# Memory Trick
# ==========================================================

# Class      -> Blueprint
# Object     -> Real thing made from the blueprint
# self       -> Current object
# __init__   -> Constructor (runs automatically)
# Class Attr -> Shared by everyone
# Object Attr-> Belongs to one object
# Static     -> Doesn't use self
# ==========================================================