# Import necessary libraries
import pandas as pd
import numpy as np

# Create a sample DataFrame
# This DataFrame simulates transaction data with TransactionID, Region, Product, and Amount.
df = pd.DataFrame({
    'TransactionID': np.arange(1000),
    'Region' : np.random.choice(['North', 'South', 'East', 'West'], 1000),
    'Product' : np.random.choice(['A', 'B', 'C','D'], 1000),
    'Amount' : np.random.randint(0, 1000, 1000) * 100
})

# Group by Region and Product, then calculate total and average Amount
# This section is intended to demonstrate grouping, but the aggregation is not performed.
# A commented-out example of how to do this:
# grouped_data = df.groupby(['Region', 'Product'])['Amount'].agg(['sum', 'mean'])
# print(grouped_data)

# Memory optimization by converting object type to category
# This is useful for columns with a limited number of unique values.
intial_memory = df['Region'].memory_usage(deep=True)
df['Region'] = df['Region'].astype('category')
optimized_memory = df['Region'].memory_usage(deep=True)

# Print memory usage before and after optimization to show the effect.
print(f"Memory usage before optimization: {intial_memory} bytes")
print(f"Memory usage after optimization: {optimized_memory} bytes\n")

# Create a pivot table to count the number of transactions by Region and Product.
# `observed=False` ensures that all categories are shown, even if they have no data.
pivot_table = df.pivot_table(values='Amount', index='Region', columns='Product', aggfunc='count', observed=False)
print("\nPivot Table (Count of Transactions by Region and Product):")
print(pivot_table)

# Filter the pivot table to show only products 'A' with a count greater than 50.
print("\nFiltered Pivot Table (Product 'A' with count > 50):")
filtered_pivot = pivot_table[pivot_table['A'] > 50]['A'].dropna()
print(filtered_pivot)

# Bin the 'Amount' column into 4 equal-sized intervals.
# This is useful for segmenting continuous data.
print("\nBinned Amounts:")
binned_amounts = pd.cut(df['Amount'], bins=4)
df['Sales_Bin'] = binned_amounts
# Display the first 5 rows with the original Amount and the new Sales_Bin.
print(df[['Amount', 'Sales_Bin']].head())

# Group by the new 'Sales_Bin' and 'Region' to count sales in each segment.
# `unstack` pivots the 'Region' index level to become columns.
# `fill_value=0` replaces any NaN values with 0.
print("\nSales Count by Sales Bin and Region:")
sales_count = df.groupby(['Sales_Bin', 'Region'], observed=False).size().unstack(fill_value=0)
print(sales_count)
