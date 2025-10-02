# This script performs a risk analysis on simulated financial data.
# It uses numpy to generate random daily returns and prices, and pandas to store and manipulate the data.
# The script defines a function to classify risk, applies it to the data, and then performs grouping and filtering operations.

import numpy as np
import pandas as pd

# Set a seed for the random number generator for reproducibility.
np.random.seed(42)
# Generate 100 random numbers from a uniform distribution between -0.05 and 0.05 for daily returns.
returns = np.random.uniform(-0.05,0.05,100)
# Generate 100 random numbers from a uniform distribution between 10 and 50 for prices.
prices = np.random.uniform(10,50,100)
# Create a pandas DataFrame to store the returns and prices.
df = pd.DataFrame({'Daily_Returns':returns,'Price':prices})

def classify_risk(daily_return:float) -> str:
    """
    Classifies the risk based on the daily return.
    - Returns > 0.01 are 'High Gain'
    - Returns < -0.01 are 'High Loss'
    - Otherwise, 'Low Volatility'
    """
    if daily_return > 0.01:
        return 'High Gain'
    elif daily_return < -0.01:
        return 'High Loss'
    else:
        return 'Low Volatility'

# Apply the 'classify_risk' function to each element in the 'Daily_Returns' Series.
# A new column 'Risk Class' is created to store the results.
df['Risk Class'] = df['Daily_Returns'].apply(classify_risk)
print(df)
print("\n-----------------------------------------------")

# Group the DataFrame by the 'Risk Class' column and count the number of occurrences in each group.
risk_counts = df.groupby('Risk Class').size()
print(risk_counts)
print("\n-----------------------------------------------")

# Create a boolean mask to filter for rows where 'Risk Class' is 'High Loss'.
boolean_mask = df['Risk Class'] == 'High Loss'
# Apply the mask to the DataFrame to get a new DataFrame with only 'High Loss' trades.
high_loss_df = df[boolean_mask]
print(high_loss_df)

