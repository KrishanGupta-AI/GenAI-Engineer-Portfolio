a = int(input("Enter your age : "))
if (a>=18):
    print("You are eligible to vote")
    print("Please Vote!")

elif (0>=a):
    print("Enter a valid age.")

else:
    print("You are not eligible for voting.")
    print("Bye Bye!")


b = int(input("Enter your age : "))
if (b>=18):
    print("Yes")
else:
    print("No")    

#RELATIONAL OPERATORS : Relational Operators are used to evaluate conditions inside the if statements.
#E.g. : == Equals , >= greater than / Equal to , <= Lesser than or equal to.

#LOGICAL OPERATORS : Logical operators operate on conditional statements.
#E.g. : and ---> True if both the operands are true.
#or ---> true if at least one operand is true.
#not ---> inverts true to false.

#ELIF Clause : Elif in python means[Else if] An if statements can be chained together with a lot of these Elif statements followed by an Else statement.

#IMPORTANT NOTES :
# 1.)There can be any number of Elif Statements.
# 2.)Last else is executed only if all the conditions inside Elifs fail.
