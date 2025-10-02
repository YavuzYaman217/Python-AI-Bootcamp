# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create a sample DataFrame.
# This data represents a simple relationship where the sale price of a house decreases as the days on the market increase.
data = pd.DataFrame({
    'DaysOnMarket': [10, 20, 30, 40, 50, 60, 70, 80],
    'SalePrice': [150, 140, 130, 120, 110, 100, 90, 80]
})

# Define the feature (X) and the target (y).
# 'DaysOnMarket' is the feature we will use to predict the 'SalePrice'.
X = data[['DaysOnMarket']]
y = data['SalePrice']

# Split the data into training and testing sets.
# 80% of the data will be used for training the model, and 20% will be used for testing its performance.
# `random_state=42` ensures that the split is the same every time the code is run, for reproducibility.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Print the shapes of the training and testing sets to verify the split.
print("Data shapes after splitting:")
print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}\n")

# Initialize the Linear Regression model.
model = LinearRegression()
# Train the model using the training data.
model.fit(X_train, y_train)

# Make predictions on the test data.
y_pred = model.predict(X_test)

# Print the real and predicted values to compare them.
print("Predictions on test data:")
print("Real values:", y_test.values)
print("Predicted values:", y_pred)

# Calculate the Mean Squared Error (MSE) to evaluate the model's performance.
# MSE measures the average of the squares of the errors—that is, the average squared difference between the estimated values and the actual value.
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

