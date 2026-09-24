a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))
d = int(input("Enter a number : "))

if (a >= b and a >= c and a >= d):
    print("a is the largest of the four numbers")

elif (b >= a and b >= c and b >= d):
    print("b is the largest of the four numbers")

elif (c >= b and c >= a and c >= d):
    print("c is the largest of the four numbers")

elif (d >= b and d >= c and d >= a):
    print("d is the largest of the four numbers")

marks_1 = int(input("enter your marks : "))
marks_2 = int(input("enter your marks : "))
marks_3 = int(input("enter your marks : "))

mean_marks = ((marks_1+marks_2+marks_3)/300)*100
print(mean_marks)

if(marks_3 > 33 and marks_1 > 33 and marks_2 > 33 and mean_marks > 40 ):
    print("Pass in all subjects")

else: 
     print("Fail") 


p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "Click this"

message = input("Enter your comment : ")
if (p1 in message or p2 in message or p3 in message or p4 in message):
     print("Spam Comment")

else :
     print("Not Spam")

username = input("Enter your username : ")

length_of_username = len(username)

if(length_of_username > 10) : 
    print("contains more than 10 characters.")
else:
    print("Contains less than 10 characters.")    

list = ["Krishan" , "Manan" , "Pushkar" , "Rohit"]

name = input("Enter your name : ")
if(name in list):
    print("List contains the following name.")
else:
    print("List does not contain the name.")    

marks_scored = int(input("Enter marks scored : "))
if(100>= marks_scored > 90):
    print("Excellent")
elif(90>= marks_scored > 80):
    print("A")
elif(80>= marks_scored > 70):
    print("B")
elif(70>= marks_scored > 60):
    print("C")
elif(60>= marks_scored > 50):
    print("D")
elif(50>= marks_scored):
    print("F")               

post = input("Enter your post : ")

if("Harry".lower() in post.lower()):
    print("Harry is present.")    
else:
    print("Harry is not present.")    