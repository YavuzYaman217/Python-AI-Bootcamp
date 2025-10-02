# Import necessary libraries for data manipulation, plotting, and machine learning.
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Load the 'tips' dataset from seaborn.
df = sns.load_dataset('tips')
# Convert categorical variables into dummy/indicator variables.
# `drop_first=True` is used to avoid multicollinearity by removing the first category of each feature.
df = pd.get_dummies(df, drop_first=True)

# --- Data Visualization ---
# Create a scatter plot to visualize the relationship between 'total_bill' and 'tip'.
plt.figure(figsize=(10, 6))
plt.title('Total Bill vs Tip')
sns.scatterplot(x='total_bill', y='tip', data=df)
print("Scatter plot of Total Bill vs Tip is being displayed.")
# Show the plot.
plt.show()

# --- Feature and Target Selection ---
# Define the features (X) by dropping the target column 'tip'.
X = df.drop(columns=['tip'], axis=1)
# Define the target variable (y).
y = df['tip']

# --- Data Splitting ---
print("\nSplitting data into training and testing sets...")
# Split the data into training (80%) and testing (20%) sets.
# `random_state=42` ensures reproducibility of the split.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Model Training and Prediction ---
# Initialize the Linear Regression model.
model = LinearRegression()
# Train the model on the training data.
model.fit(X_train, y_train)
# Make predictions on the test data.
y_pred = model.predict(X_test)

# --- Model Evaluation ---
# Calculate the Mean Absolute Error (MAE) to evaluate the model.
# MAE is the average of the absolute differences between predicted and actual values.
mae = mean_absolute_error(y_test, y_pred)
print("Model trained and predictions made.")
# Print the actual and predicted values for comparison.
print(f"Real values (first 5): {y_test.values[:5]}")
print(f"Predicted values (first 5): {y_pred[:5]}")
# Print the MAE, formatted to two decimal places.
print(f"Mean Absolute Error: {mae:.2f}")