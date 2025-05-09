import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Step 1: Data Load
df = pd.read_csv('Global_Superstore.csv', encoding='latin1')

# Step 2: Data Cleaning
df.drop_duplicates(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')
df.dropna(subset=['Order Date', 'Sales', 'Profit', 'Region', 'Category'], inplace=True)

# Step 3: Feature Engineering
df['Month'] = df['Order Date'].dt.to_period('M')
df['Year'] = df['Order Date'].dt.year

# Step 4: Grouping Data
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
category_profit = df.groupby('Category')['Profit'].sum().sort_values()
monthly_sales = df.groupby('Month')['Sales'].sum()

# Step 5: Output Folder Ensure
output_dir = 'output_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Step 6: Visualizations
sns.set(style="whitegrid")

# Region-wise Sales
plt.figure(figsize=(8,5))
sns.barplot(x=region_sales.values, y=region_sales.index, palette='Blues_d')
plt.title('Total Sales by Region')
plt.xlabel('Sales')
plt.ylabel('Region')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'region_sales.png'))
plt.show()

# Category-wise Profit
plt.figure(figsize=(8,5))
sns.barplot(x=category_profit.values, y=category_profit.index, palette='RdYlGn')
plt.title('Total Profit by Category')
plt.xlabel('Profit')
plt.ylabel('Category')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'category_profit.png'))
plt.show()

# Monthly Sales Trend
plt.figure(figsize=(12,6))
monthly_sales.sort_index().plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'monthly_sales_trend.png'))
plt.show()
