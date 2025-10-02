# Import necessary libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset from seaborn's built-in datasets.
df_iris = sns.load_dataset('iris')
# Print the first 5 rows to inspect the data.
print("First 5 rows of the Iris dataset:")
print(df_iris.head())

# --- Box Plot ---
# A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables.
plt.figure(figsize=(10, 6))
# Create a box plot showing the distribution of 'sepal_length' for each 'species'.
sns.boxplot(x='species', y='sepal_length', data=df_iris)
# Set the title of the plot.
plt.title('Box Plot of Sepal Length by Species')
# Display the plot.
plt.show()

# --- Histogram ---
# A histogram represents the distribution of a single numerical variable.
plt.figure(figsize=(10, 6))
# Create a histogram of 'sepal_length'.
# `kde=True` adds a Kernel Density Estimate line to smooth the distribution.
sns.histplot(data=df_iris, x='sepal_length', kde=True)
# Set the title of the plot.
plt.title('Histogram of Sepal Length')
# Set the labels for the axes.
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
# Display the plot.
plt.show()

# --- Joint Plot ---
# A joint plot shows the relationship between two variables (a scatter plot) and their individual distributions (histograms).
# Create a joint plot for 'sepal_length' and 'sepal_width'.
# `kind='scatter'` specifies a scatter plot for the joint distribution.
# `hue='species'` colors the points by species.
sns.jointplot(x='sepal_length', y='sepal_width', data=df_iris, kind='scatter', hue='species')
# Set a title for the entire figure. `y=1.02` adjusts the title's vertical position.
plt.suptitle('Joint Plot of Sepal Length vs Sepal Width', y=1.02)
# Display the plot.
plt.show()

# --- Heatmap ---
# A heatmap is a graphical representation of data where values are depicted by color.
print("\nHeatmap of the Iris dataset correlation matrix:")
plt.figure(figsize=(8, 6))
# Calculate the correlation matrix for the numeric columns of the dataset.
corr = df_iris.corr(numeric_only=True)
# Create a heatmap of the correlation matrix.
# `annot=True` displays the correlation values on the heatmap.
# `cmap='coolwarm'` sets the color map.
# `fmt=".2f"` formats the annotation values to two decimal places.
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
# Set the title of the plot.
plt.title('Heatmap of Iris Dataset Correlation')
# Display the plot.
plt.show()
# Print the correlation matrix.
print(corr)
