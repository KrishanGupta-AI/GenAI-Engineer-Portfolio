# ==========================================
# TASK 1 : Discount Rules (if / elif / else)
# ==========================================

try:
    order_amount = int(input("Enter Order Amount: "))
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

if order_amount >= 2000:
    discount = 15
elif order_amount >= 1500:
    discount = 10
elif order_amount >= 1000:
    discount = 7
else:
    discount = 0

discount_amount = order_amount * discount / 100
subtotal = order_amount - discount_amount
tax = subtotal * 5 / 100
final_amount = subtotal + tax

print("\n----- Bill -----")
print("Order Amount :", order_amount)
print("Discount     :", discount, "%")
print("Subtotal     :", subtotal)
print("Tax (5%)     :", tax)
print("Final Amount :", final_amount)


# ==========================================
# TASK 2 : Process Multiple Orders (for loop)
# ==========================================

orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discount_count = 0

print("\n========== Order Summary ==========")
print("Order\tDiscount\tFinal Amount")

for order in orders:

    if order >= 2000:
        discount = 15
    elif order >= 1500:
        discount = 10
    elif order >= 1000:
        discount = 7
    else:
        discount = 0

    final = order - (order * discount / 100)

    print(order, "\t", str(discount) + "%", "\t\t", final)

    total_revenue += final

    if discount > 0:
        discount_count += 1

print("\nTotal Revenue :", total_revenue)
print("Orders with Discount :", discount_count)


# ==========================================
# TASK 3 : User Menu (while loop)
# ==========================================

orders = []

while True:

    print("\n========== MENU ==========")
    print("1. Add Order")
    print("2. Show Orders")
    print("q. Quit")

    choice = input("Enter Choice: ")

    if choice == "1":
        amount = int(input("Enter Order Amount: "))
        orders.append(amount)

    elif choice == "2":

        total = 0

        if len(orders) == 0:
            print("No Orders Available.")
            continue

        print("\nOrder\tDiscount\tFinal")

        for order in orders:

            if order >= 2000:
                discount = 15
            elif order >= 1500:
                discount = 10
            elif order >= 1000:
                discount = 7
            else:
                discount = 0

            final = order - (order * discount / 100)

            print(order, "\t", str(discount) + "%", "\t\t", final)

            total += final

        print("Total Amount :", total)

    elif choice == "q":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")
        continue


# ==========================================
# TASK 5 : Loop Control (break & continue)
# ==========================================

daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

print("\n========== Daily Sales ==========")

for sale in daily:

    if sale == -1:
        print("Corrupted Data Found. Stopping...")
        break

    if sale == 0:
        print("No Sales Today.")
        continue

    total_sales += sale
    print("Running Total :", total_sales)

print("Final Total Sales :", total_sales)