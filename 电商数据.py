import pandas as pd  
  
# Read the CSV file containing e-commerce data  
data = pd.read_csv('ecommerce_data.csv')  
  
# Data cleaning  
# Assuming that the data has already undergone preliminary cleaning and has no missing values or outliers  
  
# Print the head of the data  
print(data.head())  
  
# Calculate the mean and standard deviation of sales quantity and sales amount  
mean_sales = data['Sales'].mean()  
std_sales = data['Sales'].std()  
print(f'Mean Sales: {mean_sales}')  
print(f'Standard Deviation of Sales: {std_sales}')  
  
# Calculate the correlation coefficient between sales amount and purchase frequency  
correlation = data[['Sales', 'Purchases']].corr()  
print(f'Correlation Coefficient between Sales and Purchases: {correlation[0][1]}')  
  
# Split the data into high-sales and low-sales groups based on the mean plus standard deviation of sales amount  
threshold = mean_sales + std_sales  
high_sales = data[data['Sales'] > threshold]  
low_sales = data[data['Sales'] <= threshold]  
  
# Print the number of records and total sales amount for high-sales and low-sales groups  
print(f'Number of High-Sales Records: {len(high_sales)}')  
print(f'Total Sales Amount for High-Sales Records: {high_sales["Sales"].sum()}')  
print(f'Number of Low-Sales Records: {len(low_sales)}')  
print(f'Total Sales Amount for Low-Sales Records: {low_sales["Sales"].sum()}')
