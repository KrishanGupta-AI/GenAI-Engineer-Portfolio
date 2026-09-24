#Dictionary is a collection of keys-value pairs.

#Properties of Python Dictionaries :
# 1.)It is unordered.
# 2.)It is mutable.
# 3.)It is indexed.
# 4.)Cannot contain duplicate keys.

dict = {} #Empty Dictionary
marks = { "Harry" : 23,
          "Krishan" : 98,
          "Akshat" : 67}

print(marks,type(marks))
print(type(marks))

print(marks["Harry"]) #Allows indexing.

#Methods of Dictionary : 
print(marks.items())
print(marks.keys())
print(marks.values())

#Dictionary is mutable.
marks.update({"Harry":99 , "Rani" : 91})
print(marks)

print(marks.get("Shivam")) #Gives output None
#print(marks["Shivam"]) #Gives error.


#Set is a collection of non - repititive elements.
sot = {1,2,3,4,5,6,7,8,9,90,"Krishan"}
print(sot)
sot.add(256)
print(sot)
print(type(sot))
#Properties of sets : 
# 1.)Sets are unordered.
# 2.)Sets are uniindexed.
# 3.)There is no way to cgange items in sets
# 4.)Sets cannot contain duplicate values.
s = set() #Empty Set

s1 = {1,2,3,4}
s2 = {4,5,6,7}
print(s1.union(s2))
print(s1.intersection(s2))