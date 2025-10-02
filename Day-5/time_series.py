# Import necessary libraries
import pandas as pd
import numpy as np

# Create a date range for 100 days starting from '2025-10-02'.
dates = pd.date_range('2025-10-02', periods=100, freq='D')
# Generate a random walk price series.
prices = np.random.randn(100).cumsum() + 50
# Create a DataFrame with the dates and prices.
df_ts = pd.DataFrame({'Date': dates, 'Price': prices})
# Convert the 'Date' column to datetime objects and set them to UTC timezone.
df_ts['Date'] = pd.to_datetime(df_ts['Date'], utc=True)
# Set the 'Date' column as the index of the DataFrame.
df_ts.set_index('Date', inplace=True)

# Display the first 5 rows of the time series data.
print("First 5 rows of the time series data:")
print(df_ts.head())

# Filter the data to show only the records from October 2025.
print("\nFiltered data for the month of October 2025:")
october_data = df_ts.loc['2025-10']
# Display the last 3 rows of the filtered data.
print(october_data.tail(3))

# Resample the data to a monthly frequency and calculate the mean price for each month.
print("\nResampled data (monthly average price):")
monthly_avg = df_ts['Price'].resample('ME').mean()
print(monthly_avg)

# Resample the data to a weekly frequency and find the maximum price for each week.
print("\nMaximum Price in the time series data (weekly):")
weekly_max_price = df_ts['Price'].resample('W').max()
# Display the first 5 weeks of the resampled data.
print(weekly_max_price.head())

# Create a new column 'Price_Prev_Day' that contains the price from the previous day.
print("\nPrice previous day data:")
df_ts['Price_Prev_Day'] = df_ts['Price'].shift(1)
# Display the last 5 rows to show the shifted data.
print(df_ts.tail())