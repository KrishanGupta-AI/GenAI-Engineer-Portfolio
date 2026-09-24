s = set()
for i in range(9):
    shivam = int(input("Enter a number : "))
    s.add(shivam)

print(s)

dictionary = {}
for i in range(4):
    name = input("Enter your name : ")
    language = input("Enter your language : ")
    dictionary.update({name:language})
print(dictionary)

#Sets cannot list in them as list is mutable in nature while set is not.