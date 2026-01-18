import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("data/sales_data.xlsx")
print(df.head())

#check how many colums in excel
print(df.columns)

#check data information
print(df.info())

#check how many values missing 
print(df.isnull().sum())

df["Quantity"].fillna(df["Quantity"].mean(),inplace=True)
df["Sales"].fillna(df["Sales"].mean(),inplace=True)
print(df.isnull())

print(df.duplicated().sum())
print(df[df.duplicated()])
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())
total_sales = df["Sales"].sum()

# --- Top Selling Product ---
product_summary = df.groupby("Product")["Sales"].sum()
top_product = product_summary.idxmax()
top_product_sales = product_summary.max()

#  Dashboard size
plt.figure(figsize=(14, 6))
plt.suptitle('Sales Performance Dashboard - AGNEYRA', fontsize=16, fontweight='bold')
plt.figtext(
    0.5, 0.90,
    f"Total Sales: ₹{total_sales:,.2f} | Top Product: {top_product} (₹{top_product_sales:,.2f})",
    ha="center",
    fontsize=11,
    color="darkgreen"
)

# --- Total Sales by Product (Bar Chart) ---
plt.subplot(1, 2, 1) # (1 row, 2 columns, 1st plot)
product_sales = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
product_sales.plot(kind='bar', color=['#3498db', '#e74c3c', '#2ecc71'])
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales Amount')
plt.xticks(rotation=0)

# --- Dusra Graph: Sales by Region (Pie Chart) ---
plt.subplot(1, 2, 2) 
region_sales = df.groupby('Region')['Sales'].sum()
region_sales.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['#f1c40f', '#9b59b6', '#e67e22', '#1abc9c'])
plt.title('Sales Distribution by Region')
plt.ylabel('')
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 

plt.savefig("sales_dashboard.png", dpi=300)
plt.show()
