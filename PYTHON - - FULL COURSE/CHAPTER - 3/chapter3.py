#String is a data type in python.
#String is a sequence of characters enclosed in quotes.

#String is immutable in nature.

#Slicing in python is a technique used to get a part of the string.
string = "Krishan"
print(string[0:7]) #0 will not be included but all the elememts till 7 will be included.(7 will also be included.)
print(string[1:4]) 
print(string[-4:-1]) 

#Easy - Trick : 1:4 = -4:-1

print(string[0:7:2]) #0 will not be included but 7 will be included.2 means that it will leave 1 element in between and select the second element.
print(len(string)) #Used to know the length of variable

print(string.startswith("Kri"))
print(string.endswith("han"))
print(string.endswith("hfan"))

