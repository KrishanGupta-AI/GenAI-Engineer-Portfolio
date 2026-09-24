number = int(input("Enter a number :"))
for i in range(11):
    print(f"{number}*{i} = {number*i}")

l = ["Harry" , "Soham" , "Sachin" , "Rahul"]
i = 0
for name in l:
    if (name.startswith("S")):
     print("Hello",name)
    else:
       continue 

number = int(input("Enter a number :"))
i = 0 
while i < 11:
   print(f"({number}*{i} = {number * i})")   
   i += 1 

number = int(input("Enter a number :"))
if number %2 == 0:
   print("It is a prime number.")
else :
   print("It is not a prime number")   

n = int(input("Enter the natural number upto which you want the sum : ")) 
i = 0 
sum = 0
while (i<=n):
   sum += i
   i += 1
print("sum of natural numbers is:",sum)   


x = int(input("Enter the natural number whose factorial you want : "))
factorial = 1
for i in range(1,x+1):
 factorial = factorial * i
 i += 1
print("Factorial of the given number is :",factorial)

n = int(input("Enter the number :"))
for i in range(1,n+1):
  print(" "*(n-i),end = "")    #We use (end = "") to not get a new line by default.
  print("*"*(2*i-1),end = "")
  print("")

n = int(input("Enter the number :"))
for i in range(1,n+1):
  print("*"*(2*i-1))

n = int(input("Enter the number :"))
for i in range(1,n+1):
  if(i==1 or i==n):
    print("*"* n ,end ="")
  else:
    print("*",end = "")
    print(" "*(n-2),end = "") 
    print("*",end ="")
  print("") 

n = int(input("Write a number whose multiplication you want to be done :"))
for i in range(1,11):
  print(f"{n}*{11 - i} = {n*(11-i)}")
  
