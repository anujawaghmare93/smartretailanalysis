import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('data/cleaned/sample_superstore.csv')

# Convert date
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Monthly Sales
monthly_sales = df.groupby(
    df['Order Date'].dt.to_period('M')
)['Sales'].sum()

# Plot Forecast Trend
plt.figure(figsize=(12,6))

monthly_sales.plot()

plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')

plt.show()