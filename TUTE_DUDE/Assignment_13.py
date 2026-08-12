# ============================================================
# A13 - DATA GATHERING, PREPROCESSING & EDA
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
import requests
from sklearn.preprocessing import LabelEncoder

sns.set_style("whitegrid")

# ============================================================
# PART 1 - DATA GATHERING
# ============================================================

# ==========================
# TASK 1 - LOAD CSV
# ==========================

print("\n========== TASK 1 ==========")

df = pd.read_csv("your_dataset.csv")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistics:")
print(df.describe())

# ==========================
# TASK 2 - LOAD JSON
# ==========================

print("\n========== TASK 2 ==========")

json_df = pd.read_json("sample.json")

print(json_df)

# ==========================
# TASK 3 - SQLITE DATABASE
# ==========================

print("\n========== TASK 3 ==========")

conn = sqlite3.connect("sample.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
id INTEGER,
name TEXT,
department TEXT,
salary INTEGER
)
""")

cursor.execute("DELETE FROM employees")

employees = [
(1,"Rahul","IT",50000),
(2,"Amit","HR",45000),
(3,"Neha","Sales",55000),
(4,"Riya","Finance",60000),
(5,"Karan","IT",65000)
]

cursor.executemany(
"INSERT INTO employees VALUES (?,?,?,?)",
employees
)

conn.commit()

employee_df = pd.read_sql(
"SELECT * FROM employees",
conn
)

print(employee_df)

conn.close()

# ==========================
# TASK 4 - TMDB API
# ==========================

print("\n========== TASK 4 ==========")

API_KEY = "YOUR_API_KEY"

url = f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"

try:

    response = requests.get(url)

    data = response.json()["results"]

    movie_df = pd.DataFrame(data)[
        [
            "title",
            "release_date",
            "vote_average",
            "popularity",
            "original_language"
        ]
    ]

    print(movie_df.head())

    movie_df.to_csv("tmdb_movies.csv",index=False)

except:
    print("API Key Required")

# ============================================================
# PART 2 - DATA PREPROCESSING
# ============================================================

# ==========================
# TASK 5 - UNDERSTANDING DATA
# ==========================

print("\n========== TASK 5 ==========")

print(df.shape)

print(df.dtypes)

print("\nMissing Values")

print(df.isnull().sum())

print("\nNumerical Columns")

print(df.select_dtypes(include=np.number).columns)

print("\nCategorical Columns")

print(df.select_dtypes(include="object").columns)

# ==========================
# TASK 6 - DATA CLEANING
# ==========================

print("\n========== TASK 6 ==========")

num_cols = df.select_dtypes(include=np.number).columns

cat_cols = df.select_dtypes(include="object").columns

for col in num_cols:
    df[col].fillna(df[col].median(),inplace=True)

for col in cat_cols:
    df[col].fillna(df[col].mode()[0],inplace=True)

df.drop_duplicates(inplace=True)

df.columns = df.columns.str.lower().str.replace(" ","_")

print(df.head())

# ==========================
# TASK 7 - FEATURE PREPARATION
# ==========================

print("\n========== TASK 7 ==========")

encoder = LabelEncoder()

for col in cat_cols:

    if col in df.columns:

        df[col] = encoder.fit_transform(df[col])

print(df.head())

# Replace target_column with your target

target = "target_column"

if target in df.columns:

    X = df.drop(target,axis=1)

    y = df[target]

    print(X.head())

    print(y.head())

# ============================================================
# PART 3 - EDA
# ============================================================

# ==========================
# TASK 8 - UNIVARIATE ANALYSIS
# ==========================

print("\n========== TASK 8 ==========")

for col in num_cols:

    if col in df.columns:

        plt.figure(figsize=(6,4))

        sns.histplot(df[col],kde=True)

        plt.title(col)

        plt.show()

for col in cat_cols:

    if col in df.columns:

        plt.figure(figsize=(6,4))

        sns.countplot(x=df[col])

        plt.title(col)

        plt.show()

for col in num_cols:

    if col in df.columns:

        plt.figure(figsize=(6,4))

        sns.boxplot(x=df[col])

        plt.title(col)

        plt.show()

# ==========================
# TASK 9 - BIVARIATE ANALYSIS
# ==========================

print("\n========== TASK 9 ==========")

if len(num_cols)>=2:

    plt.figure(figsize=(6,5))

    sns.scatterplot(
        data=df,
        x=num_cols[0],
        y=num_cols[1]
    )

    plt.show()

plt.figure(figsize=(10,8))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.show()

if len(cat_cols)>0 and len(num_cols)>0:

    sns.barplot(
        data=df,
        x=cat_cols[0],
        y=num_cols[0]
    )

    plt.xticks(rotation=45)

    plt.show()

    sns.boxplot(
        data=df,
        x=cat_cols[0],
        y=num_cols[0]
    )

    plt.xticks(rotation=45)

    plt.show()

# ==========================
# TASK 10 - INSIGHTS
# ==========================

print("\n========== TASK 10 ==========")

print("""
1. Checked missing values.
2. Removed duplicate rows.
3. Converted categorical data into numeric.
4. Visualized numerical distributions.
5. Visualized categorical distributions.
6. Observed outliers using boxplots.
7. Checked correlation using heatmap.
8. Compared numerical and categorical features.
9. Dataset is ready for Machine Learning.
10. Saved cleaned dataset if required.
""")