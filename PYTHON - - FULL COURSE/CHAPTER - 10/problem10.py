class Programmer():
    company_name  = "Microsoft"
    def __init__(self,name,Salary,role):
         self.name = name 
         self.Salary = Salary
         self.role = role

    def getinfo(self):
        print(f"My name is {self.name} and my salary is {self.Salary} and my role in company is {self.role}")

Krishan = Programmer("Krishan" , 200000000 , "Gen AI Engineer")
Krishan.getinfo()

number = int(input("Enter number on which you want the operation to occur."))
class Calculator:

    def __init__(self,number):
        self.number = number

    @staticmethod
    def greet():
        print("Hello User")    

    def square(self):
        square_of_number  = self.number * self.number
        print(f"Square of given number is {square_of_number}")

    def square_root(self):
        square_root = self.number**1/2    
        print(f"Square root of given number is {square_root}")

Number = Calculator(number)
Number.square_root()
Number.square()       
Number.greet() 

class Demo():
    a = 4

o = Demo()
o.a = 3  #It changes only the instance attribute and not the class attribute

print(o.a)
print(Demo.a)


from random import randint
class Train():

    def __init__(self,fro,to):
        self.fro = fro
        self.to = to

    def book(self):
        print(f"The train is booked from {self.fro} to {self.to}.")

    def getStatus(self):
        print(f"Train is booked from {self.fro} to {self.to}")

    def getfare(self):
        print(f"The fare of the ticket is {randint(22,2567)}")

Train_details = Train("Delhi" , "Jalandhar")
Train_details.getfare()
Train_details.getStatus()
Train_details.book()