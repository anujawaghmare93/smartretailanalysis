import pandas as pd

# Load Dataset
df = pd.read_csv('data/cleaned/sample_superstore.csv')

# Remove duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna(0, inplace=True)

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Save cleaned data
df.to_csv('data/cleaned/cleaned_superstore.csv', index=False)

print("Data Cleaning Completed")
print(df.head())