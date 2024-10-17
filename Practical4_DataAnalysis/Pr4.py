import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Loading
try:
    df = pd.read_csv("./OnlineRetail.csv", encoding='ISO-8859-1')
except FileNotFoundError:
    print("The file 'Online Retail.csv' was not found. Please check the file path.")
    raise

# 2. Data Cleaning
df.dropna(subset=['CustomerID'], inplace=True)  # Drop rows with missing CustomerID
df.drop_duplicates(inplace=True)  # Remove duplicates

# Add a 'TotalAmountSpent' column (Quantity * UnitPrice)
df['TotalAmountSpent'] = df['Quantity'] * df['UnitPrice']

# 3. Feature Engineering
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')  # Convert InvoiceDate to datetime format

# Calculate Recency (days since the last purchase)
df['Recency'] = (pd.to_datetime('today') - df['InvoiceDate']).dt.days

# Calculate Total Amount Spent and Total Items Purchased by each customer
customer_data = df.groupby('CustomerID').agg({
    'TotalAmountSpent': 'sum',
    'Quantity': 'sum',
    'Recency': 'min'  # Use 'min' to get the most recent purchase
}).reset_index()

customer_data.rename(columns={'Quantity': 'TotalItemsPurchased'}, inplace=True)

# Calculate Average Purchase Value
customer_data['AveragePurchaseValue'] = customer_data['TotalAmountSpent'] / customer_data['TotalItemsPurchased']

# 4. Handle Missing or Infinite Values
customer_data.replace([np.inf, -np.inf], np.nan, inplace=True)
customer_data.dropna(inplace=True)

# 5. Descriptive Statistics
print("Descriptive Statistics for TotalAmountSpent:")
print(customer_data['TotalAmountSpent'].describe())
print("\nDescriptive Statistics for TotalItemsPurchased:")
print(customer_data['TotalItemsPurchased'].describe())

# 6. Customer Segmentation using K-means Clustering
X = customer_data[['TotalAmountSpent', 'TotalItemsPurchased', 'AveragePurchaseValue', 'Recency']]

# Apply K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42)  # Specify n_init to avoid warnings
customer_data['Segment'] = kmeans.fit_predict(X)

# 7. Visualization
plt.figure(figsize=(10, 6))
sns.scatterplot(x='TotalAmountSpent', y='TotalItemsPurchased', hue='Segment', data=customer_data, palette='viridis')
plt.title('Customer Segmentation based on Total Amount Spent and Total Items Purchased')
plt.show()

# 8. Customer Insights
insights = customer_data.groupby('Segment').mean().reset_index()
print("Customer Segment Insights:")
print(insights)

# 9. Customer Engagement Recommendations
for segment in insights['Segment']:
    print(f"\nSegment {segment} Recommendations:")
    if insights.loc[segment, 'TotalAmountSpent'] > customer_data['TotalAmountSpent'].mean():
        print("- Targeted promotions and discounts to retain high spenders.")
    if insights.loc[segment, 'Recency'] > customer_data['Recency'].mean():
        print("- Re-engagement campaigns for inactive customers.")
    if insights.loc[segment, 'TotalItemsPurchased'] > customer_data['TotalItemsPurchased'].mean():
        print("- Loyalty programs to reward frequent shoppers.")
