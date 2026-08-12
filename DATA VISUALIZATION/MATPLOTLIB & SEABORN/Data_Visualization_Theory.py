# Matplolib and Seaborn are basically used for internal purpose i.e. when we do an EDA or 
# lets say we make a machine learning model.They are not same like PowerBI or Excel , there main
# focus is to provide a simple and clean visualization , rather than creating dashboards.


# Used to import Matplotlib Library
import matplotlib.pyplot as plt

# Used to import Seaborn Library
import seaborn as sns

# WHAT is Data Visualization?
# Data Visualization is the process of representing data in a visual format such as charts, graphs, maps, and dashboards to make it easier to understand, analyze, and communicate information.
# Instead of reading large tables of numbers, data visualization helps us quickly identify patterns, trends, relationships, and outliers.

# Definition:
# "Data Visualization is the graphical representation of data using visual elements like charts, graphs, plots, and maps."

# Example:
# A table showing monthly sales may be difficult to analyze, but a line chart immediately shows whether sales are increasing or decreasing.

# ------------------------------------------------------------

# Why do we need Data Visualization?
# Data visualization is important because it helps us:

# 1. Understand large amounts of data quickly.
# 2. Identify trends over time.
# 3. Find patterns and relationships between variables.
# 4. Detect outliers or unusual values.
# 5. Compare different categories easily.
# 6. Make better business decisions.
# 7. Present findings in an attractive and understandable way.
# 8. Save time compared to reading raw data.
# 9. Communicate insights to non-technical people.
# 10. Support data-driven decision making.

# Example:
# Instead of reading 10,000 rows of sales data, a bar chart can instantly show which product sold the most.

# ------------------------------------------------------------

# How to use Data Visualization?
# Steps to use Data Visualization:

# Step 1:
# Collect the data.

# Step 2:
# Clean and preprocess the data (remove missing values, duplicates, etc.).

# Step 3:
# Understand what you want to analyze.

# Step 4:
# Choose the appropriate chart.

# Step 5:
# Create the visualization using a tool or programming library.

# Step 6:
# Interpret the chart and draw conclusions.

# Step 7:
# Share the insights with others.

# Common Python Libraries:
# • Matplotlib
# • Seaborn
# • Plotly

# Common Tools:
# • Microsoft Excel
# • Power BI
# • Tableau
# • Google Looker Studio

# ------------------------------------------------------------

# Common Types of Data Visualizations

# 1. Line Chart
# - Shows trends over time.
# Example: Monthly sales.

# 2. Bar Chart
# - Compares different categories.
# Example: Sales by product.

# 3. Pie Chart
# - Shows percentage or proportion.
# Example: Market share.

# 4. Histogram
# - Shows distribution of numerical data.
# Example: Student marks.

# 5. Scatter Plot
# - Shows relationship between two numerical variables.
# Example: Height vs Weight.

# 6. Box Plot
# - Detects outliers and shows data spread.

# 7. Heatmap
# - Shows relationships or correlations using colors.

# 8. Area Chart
# - Displays cumulative values over time.

# ------------------------------------------------------------

# # Choosing the Right Chart

# Comparison between categories → Bar Chart

# Trend over time → Line Chart

# Percentage of a whole → Pie Chart

# Distribution of data → Histogram

# Relationship between two variables → Scatter Plot

# Finding outliers → Box Plot

# Correlation between variables → Heatmap

# ------------------------------------------------------------

# Advantages of Data Visualization

# • Easy to understand
# • Faster analysis
# • Better decision making
# • Identifies hidden patterns
# • Detects anomalies
# • Improves communication
# • Makes reports more attractive
# • Helps in business intelligence

# ------------------------------------------------------------

# Limitations of Data Visualization

# • Wrong chart can give misleading results.
# • Poor design may confuse viewers.
# • Cannot replace proper statistical analysis.
# • Large datasets may require preprocessing.
# • Too many colors or labels reduce readability.

# ------------------------------------------------------------

# Applications of Data Visualization

# • Business Analytics
# • Data Science
# • Machine Learning
# • Healthcare
# • Finance
# • Marketing
# • Sports Analytics
# • Education
# • Government
# • Weather Forecasting

# ------------------------------------------------------------

# Data Visualization in Python

# Popular libraries:

# 1. Matplotlib
# - Basic plotting library.
# - Highly customizable.

# 2. Seaborn
# - Built on Matplotlib.
# - Beautiful statistical graphics.

# 3. Plotly
# - Interactive visualizations.

# 4. Bokeh
# - Interactive web-based plots.

# 5. Altair
# - Simple and declarative visualization library.

# ------------------------------------------------------------

# Best Practices

# • Choose the correct chart type.
# • Keep the design simple.
# • Add proper title.
# • Label X-axis and Y-axis.
# • Use readable colors.
# • Avoid unnecessary decorations.
# • Highlight important information.
# • Keep scales consistent.
# • Do not overload a chart with too much information.

# ------------------------------------------------------------

# Interview Questions

# Q1. What is Data Visualization?
# A. Graphical representation of data to understand patterns and insights.

# Q2. Why is Data Visualization important?
# A. It helps identify trends, patterns, and supports better decision-making.

# Q3. Name some Python libraries for Data Visualization.
# A. Matplotlib, Seaborn, Plotly, Bokeh, Altair.

# Q4. Which chart is best for showing trends?
# A. Line Chart.

# Q5. Which chart is best for comparing categories?
# A. Bar Chart.

# Q6. Which chart is best for showing relationships between two variables?
# A. Scatter Plot.

# ------------------------------------------------------------

# Key Points to Remember

# • Data Visualization converts raw data into visual form.
# • It makes data easier to understand.
# • The right chart type is essential.
# • Visualization helps in finding trends, patterns, correlations, and outliers.
# • Matplotlib and Seaborn are the most commonly used Python libraries for beginners.
# • Good visualizations lead to better business and data-driven decisions.


# Category of Plots : 
# 1.) Numerical vs Numerical : Scatter Plot , Line Plot , Area Plot
# 2.) Categorical vs Numerical : Bar Plot , Box Plot , Violin Plot
# 3.) Categorical vs Categorical : Stacked Bar Plot , Mosaic Plot , Heatmap
# 4.) Time Series Data : Line Plot , Area Plot , Candlestick Chart
# 5.) Geospatial Data : Choropleth Map , Scatter Geo Plot , Heatmap on Map
# 6.) Hierarchical Data : Treemap , Sunburst Chart , Dendrogram
# 7.) Network Data : Network Graph , Force-Directed Graph , Chord Diagram
# 8.) Multivariate Data : Pair Plot , Parallel Coordinates Plot , Andrews Curves
# 9.) Distribution Data : Histogram , Density Plot , Box Plot
# 10.) Proportional Data : Pie Chart , Donut Chart , Stacked Area Plot
# 11.) Text Data : Word Cloud , Bar Chart of Word Frequencies , Heatmap of Word Co-occurrences                                                  
