# ==========================================
# TASK 1 : math_utils Module
# ==========================================

import math_utils
from math_utils import square

print("Addition:", math_utils.add(10, 5))
print("Subtraction:", math_utils.subtract(10, 5))
print("Square:", square(6))


# ==========================================
# TASK 2 : string_utils Module
# ==========================================

import string_utils

text = "welcome to python"

print("\nCapitalized:", string_utils.capitalize_words(text))
print("Reverse:", string_utils.reverse_string(text))
print("Word Count:", string_utils.word_count(text))


# ==========================================
# TASK 3 : shop_package Package
# ==========================================

from shop_package import apply_discount
from shop_package import flat_discount
from shop_package import calculate_total
from shop_package import apply_tax

price = 1000

print("\nDiscounted Price:", apply_discount(price, 10))
print("Flat Discount:", flat_discount(price))

prices = [100, 200, 300]

total = calculate_total(prices)

print("Total Bill:", total)
print("Bill After Tax:", apply_tax(total))


# ==========================================
# TASK 4 : Importing Package
# ==========================================

import shop_package.discount as disc
from shop_package.billing import calculate_total

print("\nTask 4 Output")
print(disc.apply_discount(1000, 10))
print(disc.flat_discount(1000))
print(calculate_total([100, 200, 300]))
print(apply_tax(calculate_total([100, 200, 300])))