# Fruits
fruits = []

for i in range(3):
    fruit = input("Enter a fruit: ")
    fruits.append(fruit)

print("Fruits:", fruits)

# Marks
list_of_marks = []

for i in range(3):
    mark = int(input("Enter marks: "))
    list_of_marks.append(mark)

list_of_marks.sort()
print("Sorted marks:", list_of_marks)

# Sum
list_numbers = [1, 2, 3, 4]
print("Sum:", sum(list_numbers))

# Count zeros
a = (7, 0, 8, 0, 0, 9)
print("Number of zeros:", a.count(0))