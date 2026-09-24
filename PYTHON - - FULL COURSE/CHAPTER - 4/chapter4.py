#Lists are containers to store a set of values of any data type.

friends = ["Apple","Banana","Cherry",345,65,7.8,True]
print(friends)

#List can also be indexed just like a string.
print(friends[2])

#List is mutable in nature.
friends[2] = "Akshat"
print(friends)

#list.append("element") adds element at the end of the list.
friends.append("Lovish")
print(friends)

#List Methods :
# 1.) sort ---> arrange in ascending order.
# 2.) reverse ---> reverse the string
# 3.) insert ---> Insert a new element at a given position (index position , element)
# 4.) pop ---> Deletes the element from the specified solution.
# 5.) remove ---> Deletes the given value from the list.(Only the first appeared value)

list = [2,3,4,5,3,4,67]
list.remove(3)
print(list)


#Tuple is an immutable data type in python.
tuple = (1,2,3,"Krishan",445,7,True,4.55,3)
print(type(tuple))
print(tuple.index(3))
#Tuple Methods :

# 1.) count ---> Tells the number of times the element has been repeated in the tuple.
# 2.) index ---> Tells the index number of the element to be found.(Tells the index position of the first desired element in the list and not the position of all the repetitive desired elements.)

print(tuple.index(3))