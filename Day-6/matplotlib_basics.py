# Import the pyplot module from matplotlib for plotting and numpy for numerical operations.
import matplotlib.pyplot as plt
import numpy as np

# --- Sine Wave Plot ---

# Generate an array of 100 numbers from 0 to 10 to serve as the x-axis.
x = np.linspace(0, 10, 100)
# Calculate the sine of each number in the x array for the y-axis.
y = np.sin(x)

# Create a new figure for the plot with a specific size (10 inches wide, 5 inches tall).
plt.figure(figsize=(10, 5))
# Plot the x and y values as a line graph.
# The 'label' will be used in the legend.
plt.plot(x, y, label='Sine Wave')
# Set the title of the plot.
plt.title('Basic Sine Wave Plot')
# Set the label for the x-axis.
plt.xlabel('X-axis')
# Set the label for the y-axis.
plt.ylabel('Y-axis')
# Display the legend on the plot.
plt.legend()
# Add a grid to the background of the plot for better readability.
plt.grid(True)
# Display the plot.
plt.show()

# --- Scatter Plot ---

# Set a seed for the random number generator for reproducibility.
np.random.seed(42)
# Generate 50 random numbers between 0 and 1 for the x-coordinates.
rand_x = np.random.rand(50)
# Generate 50 random numbers between 0 and 1 for the y-coordinates.
rand_y = np.random.rand(50)

# Create a new figure for the scatter plot with a size of 8x6 inches.
plt.figure(figsize=(8, 6))
# Create a scatter plot of the random points.
# `color='red'` sets the color of the points.
# `alpha=0.5` makes the points semi-transparent.
# `marker='o'` sets the shape of the points to circles.
# `label` is for the legend.
plt.scatter(rand_x, rand_y, color='red', alpha=0.5, marker='o', label='Random Points')
# Set the title of the plot.
plt.title('Basic Scatter Plot')
# Set the label for the x-axis.
plt.xlabel('X-axis')
# Set the label for the y-axis.
plt.ylabel('Y-axis')
# Display the legend.
plt.legend()
# Add a grid to the background.
plt.grid(True)
# Display the plot.
plt.show()
