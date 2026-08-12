import streamlit as st

# ==========================================
# TASK 1 : Basic Streamlit App
# ==========================================

st.title("Welcome to Streamlit!")

name = st.text_input("Enter your Name")

if st.button("Greet Me"):
    st.write(f"Hello, {name}!")


# ==========================================
# TASK 2 : Price Calculator
# ==========================================

st.header("Price Calculator")

price = st.number_input("Enter Product Price", min_value=0.0)

discount = st.slider("Discount Percentage", 0, 50, 10)

if st.button("Calculate Price"):

    final_price = price - (price * discount / 100)

    st.success(f"Original Price : {price}")
    st.success(f"Discount : {discount}%")
    st.success(f"Final Price : {final_price}")

    st.table([
        ["Before", price],
        ["After", final_price]
    ])


# ==========================================
# TASK 3 : Product Form
# ==========================================

st.header("Product Form")

product = st.sidebar.text_input("Product Name")

category = st.sidebar.selectbox(
    "Category",
    ["Electronics", "Clothing", "Books", "Food", "Sports"]
)

product_price = st.sidebar.number_input(
    "Price",
    min_value=0.0
)

if st.sidebar.button("Add Product"):

    st.success("Product Added Successfully!")

    st.write("### Product Details")

    st.write("Product :", product)
    st.write("Category :", category)
    st.write("Price :", product_price)


# ==========================================
# TASK 4 : Mini Dashboard
# ==========================================

st.header("Simple Sales Dashboard")

months = ["January", "February", "March", "April"]

sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000
}

selected_month = st.selectbox("Select Month", months)

st.metric("Sales", sales[selected_month])

st.bar_chart(list(sales.values()))