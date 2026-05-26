import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/cleaned/sample_superstore.csv')

# Region Sales
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(8,5))

region_sales.plot(kind='pie', autopct='%1.1f%%')

plt.title('Region Wise Sales')

plt.ylabel('')

plt.show()