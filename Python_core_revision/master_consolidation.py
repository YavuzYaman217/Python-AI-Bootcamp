# Import necessary libraries
import numpy as np  # For numerical operations and creating sample data
import pandas as pd  # For data manipulation and analysis
import seaborn as sns  # For statistical data visualization
import matplotlib.pyplot as plt  # For creating plots and charts
from sklearn.model_selection import train_test_split  # For splitting data into training and testing sets
from sklearn.linear_model import LinearRegression  # For building a linear regression model
from sklearn.metrics import mean_absolute_error  # For evaluating the model's performance

# --- 1. Data Creation and Initial Setup ---

# Set a seed for NumPy's random number generator for reproducibility.
# This ensures that the same random numbers are generated each time the code is run.
np.random.seed(2025)

# Create a dictionary to hold sample social media post data.
data = {
    'PostID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Date': ['2025-01-05', '2025-01-12', '2025-02-01', '2025-02-15', '2025-03-01', 
             '2025-03-08', '2025-03-15', '2025-04-01', '2025-04-08', '2025-04-15'],
    'Category': ['Reels', 'Story', 'Reels', 'Image', 'Reels', 'Story', 'Image', 'Reels', 'Story', 'Image'],
    'Views': [15000, 800, 22000, 4500, 18000, 950, 5000, 25000, 1000, 6000],
    'Cost': [100.0, 15.0, 120.0, 40.0, 90.0, 18.0, np.nan, 130.0, 20.0, 45.0] # Includes a missing value
}
# Create a pandas DataFrame from the dictionary.
df = pd.DataFrame(data)

# Add a new column 'Engagement_Rate' with random values between 0.01 and 0.15.
df['Engagement_Rate'] = np.random.uniform(0.01, 0.15, size=len(df))
print("Initial DataFrame:")
print(df)


# --- 2. Data Cleaning and Feature Engineering ---

# Convert the 'Date' column from string objects to datetime objects.
# `utc=True` makes the datetime objects timezone-aware (Coordinated Universal Time).
df['Date'] = pd.to_datetime(df['Date'], utc=True)

# Handle missing values in the 'Cost' column by filling the NaN with the mean of the column.
df['Cost'] = df['Cost'].fillna(df['Cost'].mean())


# Define a function to calculate Return on Investment (ROI).
def calculate_roi(views, cost):
    try:
        # ROI formula: (Revenue / Cost) * 100. Here, we use 'Views' as a proxy for revenue.
        return (views / cost) * 100
    except ZeroDivisionError:
        # Handle cases where cost is zero to avoid division errors.
        print("Cost is zero, cannot calculate ROI.")
        return 0.0
    
# Apply the ROI function to each row of the DataFrame to create a new 'ROI' column.
# `axis=1` ensures the function is applied row-wise.
df['ROI'] = df.apply(lambda row: calculate_roi(row['Views'], row['Cost']), axis=1)


# --- 3. Data Analysis and Filtering ---

# Filter the DataFrame to find posts that are 'Reels' and have more than 10,000 views.
# Then, extract the 'PostID' of these posts into a list.
filtered_df = df[(df['Category'] == 'Reels') & (df['Views'] >  10000)]['PostID'].tolist()

print("\nFiltered PostIDs (Category: Reels and Views > 10000):")
print(filtered_df)


# Group the data by 'Category' and calculate the average 'Engagement_Rate' for each.
# Convert the resulting Series to a dictionary for easy viewing.
avg_engagement_by_category = df.groupby('Category')['Engagement_Rate'].mean().to_dict()
print("\nAverage Engagement Rate by Category:")
print(avg_engagement_by_category)


# --- 4. Data Visualization ---

# Create a box plot to visualize the distribution of ROI for each post category.
plt.figure(figsize=(10, 6)) # Set the figure size for better readability.
plt.title('ROI by Category') # Set the title of the plot.
sns.boxplot(x='Category', y='ROI', data=df) # Generate the box plot using seaborn.
plt.xlabel('Category') # Label for the x-axis.
plt.ylabel('ROI (%)') # Label for the y-axis.
plt.grid(True) # Add a grid for easier value reading.
plt.show() # Display the plot.


# --- 5. Machine Learning Model ---

# Prepare the data for modeling.
# Convert the categorical 'Category' column into numerical format using one-hot encoding.
# `drop_first=True` removes the first category to avoid multicollinearity.
df = pd.get_dummies(df, columns=['Category'], drop_first=True)

# Define the features (X) and the target variable (y).
# X contains the independent variables used for prediction.
X = df.drop(['PostID', 'Date', 'Engagement_Rate', 'ROI', 'Cost'], axis=1)
# y contains the dependent variable we want to predict.
y =  df['Engagement_Rate']

# Split the data into training and testing sets.
# 80% of the data will be used for training the model, and 20% for testing its performance.
# `random_state=42` ensures the split is the same every time.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTraining data shape:")
print(f"X_train: {X_train.shape}")
print(f"X_test: {X_test.shape}\n")

# Initialize and train the Linear Regression model.
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test data.
y_pred = model.predict(X_test)
print("Predictions on test data:")
print("Real values:", y_test.values)
print("Predicted values:", y_pred)

# Evaluate the model using Mean Absolute Error (MAE).
# MAE measures the average magnitude of the errors in a set of predictions, without considering their direction.
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")




