# ==========================================
# TASK 1 : Safe Division Utility
# ==========================================

try:
    numerator = float(input("Enter Numerator: "))
    denominator = float(input("Enter Denominator: "))

    result = numerator / denominator

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Denominator cannot be zero.")

else:
    print("Result:", result)

finally:
    print("Operation Complete")


# ==========================================
# TASK 2 : Bill Calculator with Error Handling
# ==========================================

prices = [120, 350, "abc", 500, -200, 800]

total = 0

for price in prices:

    try:

        if not isinstance(price, (int, float)):
            raise TypeError("Not a number")

        if price < 0:
            raise ValueError("Negative price not allowed")

        total += price
        print("Running Total:", total)

    except TypeError as e:
        print(e)

    except ValueError as e:
        print(e)

print("Final Total:", total)


# ==========================================
# TASK 3 : Custom Exception - Age Validator
# ==========================================

def check_age(age):

    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")

    return "Valid Age"


try:

    age = int(input("Enter Age: "))
    print(check_age(age))

except ValueError as e:
    print(e)


# ==========================================
# TASK 4 : File Reader with Exception Handling
# ==========================================

filename = input("Enter Filename: ")

try:

    file = open(filename, "r")

    print("First 3 Lines:")

    for i in range(3):
        print(file.readline().strip())

    file.close()

except FileNotFoundError:
    print("File Not Found.")

except PermissionError:
    print("Permission Denied.")

finally:
    print("File operation attempted.")


# ==========================================
# TASK 5 : Mini Program - Safe Shopping Cart
# ==========================================

cart = []

while True:

    value = input("Enter Price (q to quit): ")

    if value.lower() == "q":
        break

    try:

        price = float(value)

        if price < 0:
            raise ValueError("Negative price not allowed")

        cart.append(price)

    except ValueError as e:
        print(e)

print("\nTotal Items:", len(cart))
print("Total Bill:", sum(cart))