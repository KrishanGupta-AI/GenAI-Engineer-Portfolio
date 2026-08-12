# ==========================================
# TASK 1 : Write Sales Records to a File
# ==========================================

sales = [1200, 450, 980, 1500, 3000]

file = open("sales_data.txt", "w")

for sale in sales:
    file.write(str(sale) + "\n")

file.close()

file = open("sales_data.txt", "r")
print("Sales Data:")
print(file.read())
file.close()


# ==========================================
# TASK 2 : Read File in Different Ways
# ==========================================

file = open("sales_data.txt", "r")
print("Using read():")
print(file.read())
file.close()

file = open("sales_data.txt", "r")
print("Using readline():")
print(file.readline().strip())
file.close()

file = open("sales_data.txt", "r")
lines = file.readlines()
numbers = []

for line in lines:
    numbers.append(int(line.strip()))

print("Using readlines():")
print(numbers)
file.close()


# ==========================================
# TASK 3 : Append New Sales
# ==========================================

file = open("sales_data.txt", "a")

new_sales = [5000, 2500, 1700]

for sale in new_sales:
    file.write(str(sale) + "\n")

file.close()

file = open("sales_data.txt", "r")
print("Updated File:")
print(file.read())
file.close()

file = open("sales_data.txt", "r")
print("Total Lines:", len(file.readlines()))
file.close()


# ==========================================
# TASK 4 : Generate Summary Report
# ==========================================

file = open("sales_data.txt", "r")

sales = []

for line in file:
    sales.append(int(line.strip()))

file.close()

total = sum(sales)
highest = max(sales)
lowest = min(sales)
average = total / len(sales)

print("Summary Report")
print("Total Sales:", total)
print("Highest Sale:", highest)
print("Lowest Sale:", lowest)
print("Average Sale:", average)


# ==========================================
# TASK 5 : Create Product Info File
# ==========================================

file = open("products.txt", "w")

for i in range(3):
    name = input("Enter Product Name: ")
    price = input("Enter Price: ")
    file.write(name + " | " + price + "\n")

file.close()

file = open("products.txt", "r")

print("Products File")
for line in file:
    print(line.strip())

file.close()


# ==========================================
# TASK 6 : Read File Safely
# ==========================================

import os

filename = input("Enter Filename: ")

if os.path.exists(filename):

    file = open(filename, "r")
    print(file.read())
    file.close()

else:
    print("File not found. Please check the filename.")


# ==========================================
# TASK 7 : Mini Project - Export Discounted Prices
# ==========================================

prices = {
    "Mouse": 500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive": 400,
    "Camera": 5000
}

discount = float(input("Enter Discount Percentage: "))

file = open("discount_report.txt", "w")

file.write("Product | Original Price | Discounted Price\n")

total = 0
count = 0

for product, price in prices.items():

    discounted = price - (price * discount / 100)

    file.write(product + " | " + str(price) + " | " + str(discounted) + "\n")

    total += discounted
    count += 1

average = total / count

file.write("\nTotal Items: " + str(count))
file.write("\nAverage Discounted Price: " + str(average))

file.close()

file = open("discount_report.txt", "r")
print("Discount Report")
print(file.read())
file.close()