def greatest_number(a,b,c):
    if a > b and a > c :
        print(f"{a} is the largest number.")
    elif a < b and b > c :
        print(f"{b} is the largest number.")
    elif c > b and a < c :
        print(f"{c} is the largest number.")     

greatest_number(23,8,89)

def C_to_F(temp_in_celsius):
    return (9*temp_in_celsius + 160)/5

temp_in_celsius = float(input("Enter the temprature in celsius : "))
print(f"Temprature in farenhiet is : {C_to_F(temp_in_celsius)}")


# To prevent python from printing a new line at the end of the print() function , we use end=""

def sum(n):
    if n== 1 :
        return 1 
    return sum(n - 1) + n

n = int(input("Enter a number :"))
print(f"Sum of natural number is : {sum(n)}")

def inches_to_cm(inch):
    return inch*(2.54)
    
n = float(input("Enter value in inches :"))

print(f"Your measurment in centimeter is : {inches_to_cm(n)}")


def star(n):
    if (n == 0):
        return  
    print("*" * n)
    star(n - 1)
star(3)

lists = ["Krishan","Akshat","Rakshit","Kartik","Ayush","Ritesh"]
def remove(lists,word):
    n = []
    for item in lists:
        if not (item == word):
          n.append(item.strip(word))
    return n    
name_input = input("enter your name to be removed")    
print(remove(lists, name_input))


number_table = int(input("Enter the number whose multiplication table is needed : "))
def multiplication_table(number):
    for i in range(1,11):
        print(f"{number} X {i} = {number*i}")

multiplication_table(number_table)

