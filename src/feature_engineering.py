import pandas as pd

df = pd.read_csv('data/cleaned/sample_superstore.csv')

# Profit Margin Feature
df['Profit_Margin'] = df['Profit'] / df['Sales']

# Month Feature
df['Order Month'] = pd.to_datetime(df['Order Date']).dt.month

# Year Feature
df['Order Year'] = pd.to_datetime(df['Order Date']).dt.year

# Save Updated Dataset
df.to_csv('data/cleaned/featured_superstore.csv', index=False)

print(df.head())