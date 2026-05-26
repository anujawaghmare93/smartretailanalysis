import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv('data/cleaned/sample_superstore.csv')

# Total sales by category
sales_by_category = df.groupby('Category')['Sales'].sum()

print(sales_by_category)

# Visualization
plt.figure(figsize=(8,5))

sales_by_category.plot(kind='bar')

plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Sales')

plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,6))

sns.heatmap(df.corr(numeric_only=True), annot=True)

plt.title('Correlation Heatmap')

plt.show()