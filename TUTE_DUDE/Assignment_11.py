import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load Dataset
df = pd.read_csv("sales.csv")


# ======================================================
# TASK 1 : Line Plot (Sales Trend)
# ======================================================

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(8,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()


# ======================================================
# TASK 2 : Scatter Plot
# ======================================================

plt.figure(figsize=(8,5))
plt.scatter(df["Sales"], df["Profit"])

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.show()


# ======================================================
# TASK 3 : Bar Plot (Vertical & Horizontal)
# ======================================================

category_sales = df.groupby("Category")["Sales"].sum()

# Vertical Bar Chart
plt.figure(figsize=(8,5))
plt.bar(category_sales.index, category_sales.values)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()

# Horizontal Bar Chart
plt.figure(figsize=(8,5))
plt.barh(category_sales.index, category_sales.values)

plt.title("Sales by Category")
plt.xlabel("Sales")
plt.ylabel("Category")

plt.show()


# ======================================================
# TASK 4 : Multiple Bar Plot
# ======================================================

years = ["2022", "2023", "2024"]

sales_2022 = [1200, 1500, 1800]
sales_2023 = [1000, 1300, 1700]

x = np.arange(len(years))
width = 0.35

plt.figure(figsize=(8,5))

plt.bar(x - width/2, sales_2022, width, label="Store A")
plt.bar(x + width/2, sales_2023, width, label="Store B")

plt.xticks(x, years)

plt.title("Sales Comparison")
plt.xlabel("Year")
plt.ylabel("Sales")

plt.legend()

plt.show()


# ======================================================
# TASK 5 : Stacked Bar Chart
# ======================================================

months = ["Jan", "Feb", "Mar", "Apr"]

online = [500, 600, 700, 800]
offline = [300, 400, 350, 450]

plt.figure(figsize=(8,5))

plt.bar(months, online, label="Online")
plt.bar(months, offline, bottom=online, label="Offline")

plt.title("Stacked Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.legend()

plt.show()


# ======================================================
# TASK 6 : Histogram
# ======================================================

plt.figure(figsize=(8,5))

plt.hist(df["Sales"], bins=10)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.show()


# ======================================================
# TASK 7 : Pie Chart
# ======================================================

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(7,7))

plt.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%"
)

plt.title("Category Wise Market Share")

plt.show()
