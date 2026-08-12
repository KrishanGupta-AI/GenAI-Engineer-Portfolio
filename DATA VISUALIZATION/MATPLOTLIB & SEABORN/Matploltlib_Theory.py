# Matplotlib is used for creating custom plots with a high-level API.

# Used to import Matplotlib Library
import matplotlib.pyplot as plt

# Anatomy of a Matplotlib Plot

# The anatomy of a Matplotlib plot refers to the different components that make up a graph or chart. Understanding these parts helps in creating clear, professional, and customizable visualizations.

# ------------------------------------------------------------

# Main Components of a Matplotlib Plot

# 1. Figure
# 2. Axes
# 3. Axis (X-axis & Y-axis)
# 4. Title
# 5. Labels
# 6. Ticks
# 7. Tick Labels
# 8. Grid
# 9. Legend
# 10. Plot (Line, Bar, Scatter, etc.)
# 11. Spines

# ------------------------------------------------------------

# 1. Figure

# Definition:
# The Figure is the entire window or canvas on which one or more plots are drawn.
# It is basically the sheet on which graphs are to be plotted.

# Think of it as:
# "A blank page on which graphs are placed."

# fig = plt.figure()

# ------------------------------------------------------------

# 2. Axes

# Definition:
# Axes is the area where the actual graph is drawn.

# An Axes contains:
# • X-axis
# • Y-axis
# • Title
# • Labels
# • Grid
# • Plot

# Example:
# fig, ax = plt.subplots()

# ------------------------------------------------------------

# 3. Axis

# Definition:
# An Axis is the horizontal or vertical scale of a graph.

# Types:
# • X-axis (Horizontal)
# • Y-axis (Vertical)

# Example:
# plt.xlabel("Months")
# plt.ylabel("Sales")

# ------------------------------------------------------------

# 4. Title

# Definition:
# A title describes what the graph represents.
# It is basically the name given to the graph.

# Example:
# plt.title("Monthly Sales Report")

# ------------------------------------------------------------

# 5. Axis Labels

# Definition:
# Axis labels explain what each axis represents. It is basically , the value given to the axis
# e.g. --> sales , revenue , month etc.

# Example:
# plt.xlabel("Month")
# plt.ylabel("Revenue")

# ------------------------------------------------------------

# 6. Ticks

# Definition:
# Ticks are the small marks on the X-axis and Y-axis indicating values.

# Example:
# 0   10   20   30

# Customize ticks:
# plt.xticks([1,2,3,4])
# plt.yticks([0,50,100])

# ------------------------------------------------------------

# 7. Tick Labels

# Definition:
# Tick labels are the numbers or names displayed beside the ticks.

# Example:
# Jan  Feb  Mar  Apr

# Customize:
# plt.xticks([1,2,3],["Jan","Feb","Mar"])

# ------------------------------------------------------------

# 8. Grid

# Definition:
# Grid lines help users read values more accurately.

# Example:
# plt.grid(True)

# ------------------------------------------------------------

# 9. Legend

# Definition:
# A legend identifies different datasets or lines in a graph.
# It is a small box at the right botton corner which contains information about the whole plot
# e.g.---> Which color represents which data , and so on.

# Example:
# plt.plot(x,y1,label="Sales")
# plt.plot(x,y2,label="Profit")

# plt.legend()

# ------------------------------------------------------------

# 10. Plot

# Definition:
# The plot is the actual visual representation of data.

# Examples:
# • Line Plot
# • Bar Chart
# • Scatter Plot
# • Histogram
# • Pie Chart

# Example:
# plt.plot(x,y)

# ------------------------------------------------------------

# 11. Spines

# Definition:
# Spines are the borders around the plotting area.

# There are four spines:
# • Top
# • Bottom
# • Left
# • Right

# Example:
# ax.spines['top'].set_visible(False)

# ------------------------------------------------------------

# Complete Anatomy Example

# import matplotlib.pyplot as plt

# months = ["Jan","Feb","Mar","Apr"]
# sales = [20,35,30,45]

# plt.figure(figsize=(6,4))        # Figure

# plt.plot(months, sales,
#          marker="o",
#          label="Sales")          # Plot

# plt.title("Monthly Sales")       # Title
# plt.xlabel("Months")             # X-axis Label
# plt.ylabel("Sales")              # Y-axis Label

# plt.grid(True)                   # Grid
# plt.legend()                     # Legend

# plt.show()

# ------------------------------------------------------------

# Hierarchy of Matplotlib

# Figure
# │
# ├── Axes
# │     ├── X-axis
# │     ├── Y-axis
# │     ├── Title
# │     ├── Labels
# │     ├── Grid
# │     ├── Legend
# │     ├── Plot
# │     └── Spines

# ------------------------------------------------------------

# Common Matplotlib Functions

# | Function | Purpose |
# |----------|---------|
# | plt.figure() | Create a figure |
# | plt.subplots() | Create figure and axes |
# | plt.plot() | Draw line graph |
# | plt.scatter() | Draw scatter plot |
# | plt.bar() | Draw bar chart |
# | plt.hist() | Draw histogram |
# | plt.pie() | Draw pie chart |
# | plt.title() | Add title |
# | plt.xlabel() | X-axis label |
# | plt.ylabel() | Y-axis label |
# | plt.legend() | Show legend |
# | plt.grid() | Add grid |
# | plt.xticks() | Customize X-axis ticks |
# | plt.yticks() | Customize Y-axis ticks |
# | plt.show() | Display graph |

# ------------------------------------------------------------

# Interview Questions

# Q1. What is a Figure in Matplotlib?
# A. The Figure is the entire canvas or window that contains one or more plots.

# Q2. What is an Axes?
# A. The Axes is the area where the actual graph is drawn.

# Q3. What is the difference between Figure and Axes?
# A.
# • Figure → Entire canvas.
# • Axes → Individual plotting area inside the figure.

# Q4. What is a Legend?
# A. A legend identifies different datasets plotted on the graph.

# Q5. What are Spines?
# A. Spines are the borders surrounding the plotting area.

# ------------------------------------------------------------

# Key Points to Remember

# • Figure = Entire canvas.
# • Axes = Individual graph.
# • Axis = X-axis or Y-axis.
# • Title explains the graph.
# • Labels describe the axes.
# • Ticks show scale values.
# • Grid improves readability.
# • Legend identifies plotted data.
# • Spines form the plot borders.
# • Every Matplotlib graph is drawn inside an Axes, which is contained within a Figure.


# Categorical Data (TEXT) ----> Describes groups or categories , essential for qualitative analysis.
# Examples include gender, color, or type of product. Categorical data is often represented using bar charts, pie charts, or box plots.
# Categorical data is of two types :
# 1.) Nominal Data : Nominal data represents categories without any inherent order or ranking. 
# Examples include colors (red, blue, green), types of fruits (apple, banana, orange), or gender.

# 2.) Ordinal Data : Ordinal data represents categories with a specific order or ranking.
# Examples include education levels (high school, bachelor's, master's, PhD), customer satisfaction ratings


# Numerical Data (NUMERICAL) ----> Represents measurable quantities, crucial for quantitative analysis. 
# Examples include height, weight, or sales figures. Numerical data is typically visualized using line charts, histograms, scatter plots, or area charts.

# Continuous Data : Continuous data can take any value within a range and is often measured.
# Examples include temperature, height, or time. Continuous data is typically visualized using line charts, histograms, or scatter plots.

# Discrete Data : Discrete data consists of distinct, separate values and is often counted.
# Examples include the number of students in a class, the number of cars in a parking lot, or the number of sales made. Discrete data is often visualized using bar charts or pie charts.   

# Category of Plots :
# 1.) Numerical Data : 
# 2.) Categorical Data :
# 3.) Numerical vs Numerical : Scatter Plot , Line Plot , Area Plot
# 4.) Numerical vs Categorical: Bar Plot , Box Plot , Violin Plot
# 5.) Categorical vs Categorical : Stacked Bar Plot , Mosaic Plot , Heatmap

# Univariate Analysis : Univariate analysis is suitable for analyzing a single variable , either numerical or categorical.
# It helps in understanding the distribution, central tendency, and variability of the data. 
# Common visualizations include histograms, box plots, and bar charts.
# Example: Analyzing the distribution of ages in a dataset using a histogram based on Teen , Adult , Senior Citizen.


# Bivariate Analysis : Bivariate analysis is ideal for exploring relationship between two variables, considering numerical and categorical combinations.
# It helps in identifying correlations, trends, and patterns between two variables.
# Common visualizations include scatter plots, line plots, and bar charts.
# Example: Examining the relationship between hours studied and exam scores using a scatter plot to identify trends and correlations.


# Multivriate Analysis : Multivariate analysis is ideal for understanding the complex relationship interactions among three or more variables.
# It helps in identifying patterns, correlations, and dependencies among multiple variables.
# Common visualizations include pair plots, heatmaps, and 3D scatter plots.
# Example: Analyzing the relationship between age, income, and spending habits using a 3D scatter plot to visualize how these variables interact with each other.

# Code :

# plt.figure(figsize = (5,5)) #Used to customize the size of figure accoriding to our choice.(ALways used before creating the chart).
# plt.xticks(rotation = 90 , fontsize = 20) #Used to rotate the xlabels(by any degree) and to change the font size as well.
# plt.bar(x_bar , y_bar , width = 0.8 , color = 'red') #Used to plot the bar chart and width is used to change its width while color is used to give desired color to the chart itself. Default width of bar chart is 1.
# plt.xlabel("Country" , fontsize = 30) #Used to give heading to the x label itself.
# plt.ylabel("Count" , fontsize = 30) #Used to give heading to the y label itself.



# Line chart ---> It is mainly used to show trends, changes, or growth over time.

# Bar plot   ---> It is basically used to plot categorical data.

# Pie chart  ---> It is basically used to plot proportion instead of count.

# Histogram  ---> It is basically used to demonstrate the statisticts of the data.




# Line Plot	            Numerical vs Numerical (usually time on X-axis)
# Scatter Plot	        Numerical vs Numerical ✅
# Histogram         	One Numerical Variable
# Box Plot              One Numerical Variable (or Numerical vs Categorical for grouped box plots)
# Bar Chart         	Categorical vs Numerical
# Pie Chart         	Categorical (proportions/percentages)