# ==========================================
# TASK 1 : Basic Function - Price After Discount
# ==========================================

def apply_discount(price, discount_percent=5):

    if discount_percent > 60:
        discount_percent = 60

    final_price = price - (price * discount_percent / 100)
    return final_price


print("Price After Discount")
print(apply_discount(1000, 10))
print(apply_discount(500))


# ==========================================
# TASK 2 : Recursive Function - Factorial
# ==========================================

def factorial(n):

    if n < 0:
        print("Error: Factorial not defined for negative numbers.")
        return

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("\nFactorial")
print(factorial(5))
print(factorial(0))
print(factorial(-3))


# ==========================================
# TASK 3 : Lambda Function - GST Calculator
# ==========================================

gst = lambda price: price + (0.18 * price)

print("\nGST Calculator")
print(gst(100))

final_price = lambda price, discount: (price + (0.18 * price)) - ((price + (0.18 * price)) * discount / 100)

print(final_price(1000, 10))


# ==========================================
# TASK 4 : Using map() - Apply GST
# ==========================================

prices = [100, 250, 400, 1200, 50]

prices_with_gst = list(map(gst, prices))

print("\nOriginal Prices")
print(prices)

print("Prices After GST")
print(prices_with_gst)


# ==========================================
# TASK 5 : Using filter() - Filter Products
# ==========================================

prices = [100, 250, 400, 1200, 50, 2000, 850]

greater_than_500 = list(filter(lambda x: x > 500, prices))
less_equal_500 = list(filter(lambda x: x <= 500, prices))

print("\nPrices Greater Than 500")
print(greater_than_500)

print("Prices Less Than or Equal To 500")
print(less_equal_500)


# ==========================================
# TASK 6 : Combined Utility Function
# ==========================================

def process_prices(prices):

    discounted_prices = list(map(lambda x: x - (x * 10 / 100), prices))

    filtered_prices = list(filter(lambda x: x > 300, discounted_prices))

    return discounted_prices, filtered_prices


discounted, filtered = process_prices([100, 500, 900, 50, 750])

print("\nDiscounted Prices")
print(discounted)

print("Filtered Prices")
print(filtered)


# ==========================================
# TASK 7 : Mini Problem - Menu Using Functions
# ==========================================

def add_price(prices_list, price):
    prices_list.append(price)


def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return sum(prices_list) / len(prices_list)


def get_max_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return max(prices_list)


prices_list = []

while True:

    print("\n===== MENU =====")
    print("1. Add Price")
    print("2. Show Average Price")
    print("3. Show Highest Price")
    print("q. Quit")

    choice = input("Enter Choice: ")

    if choice == "1":
        price = float(input("Enter Price: "))
        add_price(prices_list, price)

    elif choice == "2":
        print("Average Price:", get_average_price(prices_list))

    elif choice == "3":
        print("Highest Price:", get_max_price(prices_list))

    elif choice == "q":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")