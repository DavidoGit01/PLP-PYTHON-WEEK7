import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# ---------------------------
# 1. Create a fake sales dataset
# ---------------------------
np.random.seed(42)  # for reproducible random numbers

months = pd.date_range(start="2023-01-01", periods=12, freq='M')
regions = ['North', 'South', 'East', 'West']
products = ['Laptop', 'Phone', 'Tablet']

# Make a DataFrame with random sales data
data = []
for month in months:
    for region in regions:
        for product in products:
            sales = np.random.randint(50, 500)  # random sales quantity
            revenue = sales * np.random.randint(100, 1000)  # random revenue
            data.append([month, region, product, sales, revenue])

df = pd.DataFrame(data, columns=['Month', 'Region', 'Product', 'Sales', 'Revenue'])

# ---------------------------
# 2. Explore the data
# ---------------------------
print("\nFirst 5 rows:")
print(df.head())

print("\nData Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# ---------------------------
# 3. Basic Stats
# ---------------------------
print("\nBasic Stats:")
print(df.describe())

# Group by region and product
grouped = df.groupby(['Region', 'Product']).mean(numeric_only=True)
print("\nAverage Sales/Revenue by Region & Product:")
print(grouped)

# ---------------------------
# 4. Visualizations
# ---------------------------
os.makedirs('figures', exist_ok=True)

# 4.1 Line chart: Total monthly revenue over time
monthly_revenue = df.groupby('Month')['Revenue'].sum()
monthly_revenue.plot(kind='line', marker='o', title='Total Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.tight_layout()
plt.savefig('figures/monthly_revenue_linechart.png')
plt.close()

# 4.2 Bar chart: Average sales per region
avg_sales_region = df.groupby('Region')['Sales'].mean()
avg_sales_region.plot(kind='bar', title='Average Sales per Region')
plt.xlabel('Region')
plt.ylabel('Average Sales')
plt.tight_layout()
plt.savefig('figures/avg_sales_region_barchart.png')
plt.close()

# 4.3 Histogram: Distribution of Sales
df['Sales'].plot(kind='hist', bins=20, title='Distribution of Sales')
plt.xlabel('Sales')
plt.tight_layout()
plt.savefig('figures/sales_histogram.png')
plt.close()

# 4.4 Scatter Plot: Sales vs. Revenue
df.plot(kind='scatter', x='Sales', y='Revenue', title='Sales vs Revenue')
plt.tight_layout()
plt.savefig('figures/sales_vs_revenue_scatter.png')
plt.close()

print("\nPlots saved to figures/ folder.")
