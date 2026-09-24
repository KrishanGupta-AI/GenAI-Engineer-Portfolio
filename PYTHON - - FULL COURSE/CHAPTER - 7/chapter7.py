#Loops make it easy for a programmer to tell the computer which set of instructions to repeat and how!

#TYPES OF LOOP IN PYTHON :
# 1.) while loops
# 2.) for loops

#While loop ---> In while loop , the condition is checked first.If it evaluates to true , the body of the loop is executed otherwise not!
#If the loop is entered , the process of [condition check & execution] is continued until the condition becomes False.

i = 1
while(i<6):
    print(i)
    i += 1


l = [1 , "Harry" , False , "This" , "Rohan" , "Shubham" , "Shubhi"]
i = 0
while( i < len(l)):
    print(l[i])
    i += 1

#For loop is used to iterate through a sequence like list , tuple , or strings[iterables].
m = [1 , 7 , 8]
for item in m:
    print(item)

#FOR LOOP WITH ELSE ---> An optional else can be used with a for loop if the code is to be executed when the loop exhausts.

n = [ 1 , 7 , 77 , 88]

for item in n:
    print(item)
else:
    print("done")    


for i in range(100):
    if (i==34):
        break #Break is used to exit the loop right now.
    print(i)

for i in range(100):
    if(i == 34):
        continue # continue is used to skip the particular iteration
    print(i)


#Pass is a null statement in python.It instructs to do nothing.
k = [1,7,8]
for item in k :
 pass #Without pass , the program will through an error when the code is run.It is primarily used to check the output of next code.

m = [1 , 7 , 8]
for item in m:
    print(item)

