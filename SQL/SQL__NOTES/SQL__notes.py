# SQL (Structured Query Language)

# SQL (Structured Query Language) is a standard programming language used to create, manage,
# manipulate, and retrieve data stored in Relational Database Management Systems (RDBMS).

# In simple words: "SQL is a language used to communicate with databases."

# ------------------------------------------------------------

# Why do we use SQL?

# SQL is used to:

# • Store data in databases.
# • Retrieve required data quickly.
# • Insert new records.
# • Update existing records.
# • Delete unwanted records.
# • Manage database structure.
# • Perform data analysis and reporting.
# • Secure and control database access.

# ------------------------------------------------------------

# Applications of SQL

# • Data Analysis
# • Business Intelligence
# • Data Science
# • Machine Learning
# • Web Development
# • Banking & Finance
# • Healthcare
# • E-commerce
# • Inventory Management
# • Customer Relationship Management (CRM)
# • Human Resource Management
# • Reporting and Dashboard Creation

# ------------------------------------------------------------

# Popular SQL Databases

# • MySQL
# • PostgreSQL
# • SQLite
# • Microsoft SQL Server
# • Oracle Database
# • MariaDB

# ------------------------------------------------------------

# Advantages of SQL

# • Easy to learn and use.
# • Fast data retrieval.
# • Handles large datasets efficiently.
# • Standardized language across most databases.
# • Supports data security and access control.
# • Integrates with Python, Power BI, Tableau, and other analytics tools.

# ------------------------------------------------------------

# Common SQL Operations

# • CREATE – Create databases and tables.
# • INSERT – Add new records.
# • SELECT – Retrieve data.
# • UPDATE – Modify existing data.
# • DELETE – Remove records.
# • ALTER – Modify table structure.
# • DROP – Delete databases or tables.

# ------------------------------------------------------------

# Key Points to Remember

# • SQL stands for Structured Query Language.
# • It is used to communicate with relational databases.
# • SQL performs CRUD operations:
#   - Create
#   - Read
#   - Update
#   - Delete
# • SQL is an essential skill for Data Analysts, Data Scientists, Machine Learning Engineers, and Generative AI Engineers.

# ------------------------------------------------------------


# A Query is a request or command written in SQL to retrieve, insert, update, delete, or 
# manipulate data stored in a database.


# Difference Between Relational Database and Non-Relational Database

# A Relational Database is a type of database that stores data in the form of tables
# (rows and columns). The tables are related to each other using Primary Keys and Foreign Keys.

# ------------------------------------------------------------

# Why do we use Relational Databases?

# • To store structured data efficiently.
# • To maintain relationships between different tables.
# • To retrieve data quickly using SQL queries.
# • To ensure data accuracy and consistency.
# • To perform complex queries and transactions.

# ------------------------------------------------------------

# Characteristics

# • Data is stored in tables.
# • Uses rows and columns.
# • Fixed (predefined) schema.
# • Supports Primary Keys and Foreign Keys.
# • Uses SQL (Structured Query Language).
# • Follows ACID properties for reliable transactions.
# • Supports JOIN operations to combine data from multiple tables.

# ------------------------------------------------------------

# Advantages

# • Easy to organize and manage data.
# • Strong data consistency.
# • Reduces data redundancy through normalization.
# • Supports complex queries and JOIN operations.
# • High security and reliability.
# • Ideal for transactional applications.

# ------------------------------------------------------------

# Disadvantages

# • Fixed schema makes changes difficult.
# • Vertical scaling can be expensive.
# • Less suitable for unstructured or rapidly changing data.
# • Performance may decrease with extremely large distributed datasets.

# ------------------------------------------------------------

# Applications

# • Banking Systems
# • E-commerce Websites
# • Hospital Management Systems
# • Student Management Systems
# • Payroll Systems
# • Inventory Management
# • Airline Reservation Systems
# • Library Management Systems


# Non-Relational Database (NoSQL)

# A Non-Relational Database (NoSQL) is a type of database that stores data in flexible formats
# such as documents, key-value pairs, graphs, or wide-column stores. Unlike relational databases,
# it does not require a fixed table structure (schema).

# ------------------------------------------------------------

# Why do we use Non-Relational Databases?

# • To store large volumes of data.
# • To handle structured, semi-structured, and unstructured data.
# • To support high-speed read and write operations.
# • To easily scale across multiple servers.
# • To manage rapidly changing data structures.

# ------------------------------------------------------------

# Characteristics

# • Does not store data only in tables.
# • Uses a flexible (dynamic) schema.
# • Stores data as documents, key-value pairs, graphs, or wide columns.
# • Supports horizontal scaling.
# • Handles large-scale distributed systems.
# • Optimized for high performance and availability.

# ------------------------------------------------------------

# Types of Non-Relational Databases

# 1. Document Database
#    - Stores data as JSON-like documents.
#    - Example: MongoDB

# 2. Key-Value Database
#    - Stores data as key-value pairs.
#    - Example: Redis

# 3. Column-Family Database
#    - Stores data in column families instead of rows.
#    - Example: Cassandra

# 4. Graph Database
#    - Stores data as nodes and relationships.
#    - Example: Neo4j

# ------------------------------------------------------------

# Advantages

# • Flexible schema.
# • High scalability.
# • Faster for large datasets.
# • Handles structured, semi-structured, and unstructured data.
# • Suitable for real-time applications.
# • Ideal for distributed systems.

# ------------------------------------------------------------

# Disadvantages

# • Limited support for JOIN operations.
# • Complex transactions may be difficult.
# • Data consistency may vary depending on the database.
# • No standard query language across all NoSQL databases.

# ------------------------------------------------------------

# Applications

# • Social Media Platforms
# • Chat Applications
# • E-commerce Websites
# • Big Data Analytics
# • Internet of Things (IoT)
# • Recommendation Systems
# • Content Management Systems
# • Real-Time Analytics

# ------------------------------------------------------------

# Examples of Non-Relational Databases

# • MongoDB
# • Cassandra
# • Redis
# • CouchDB
# • Neo4j
# • Amazon DynamoDB

# ------------------------------------------------------------

# Example (Document Database)

#```json
# {
#   "student_id": 101,
#   "name": "Alice",
#   "age": 20,
#   "course": "AIML"
# }
# ```

# ------------------------------------------------------------

# Key Features

# • Flexible schema
# • No fixed table structure
# • Supports horizontal scaling
# • High performance
# • Suitable for distributed systems
# • Handles large and rapidly changing data

# ------------------------------------------------------------

# Interview Questions

# Q1. What is a Non-Relational Database?
# A. A Non-Relational Database stores data in flexible formats such as documents, key-value pairs, graphs, or column families.

# Q2. Why is it called NoSQL?
# A. Because it does not rely solely on traditional SQL tables and supports non-tabular data models.

# Q3. Name some Non-Relational Databases.
# A. MongoDB, Cassandra, Redis, CouchDB, Neo4j, Amazon DynamoDB.

# Q4. What type of data can a NoSQL database store?
# A. Structured, semi-structured, and unstructured data.

# ------------------------------------------------------------

