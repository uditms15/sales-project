import pandas as pd

print("📊 Sales Project Started")

# Load dataset (THIS IS REQUIRED)
df = pd.read_excel("data/Sample - Superstore.xls")

print("\nFirst 5 rows:")
print(df.head())

print("\n📊 CATEGORY ANALYSIS")

category_sales = df.groupby("Category")["Sales"].sum()
print("Sales by Category:\n", category_sales)

category_profit = df.groupby("Category")["Profit"].sum()
print("\nProfit by Category:\n", category_profit)
print("\n🏆 TOP 5 PRODUCTS BY SALES")

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)

print(top_products)
print("\n⚠️ LOSS MAKING PRODUCTS")

loss_products = df[df["Profit"] < 0][["Product Name", "Profit"]].head(10)

print(loss_products)
import matplotlib.pyplot as plt

print("\n📊 Showing Sales by Category Chart")

df.groupby("Category")["Sales"].sum().plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()
print("\n📊 Showing Profit by Category Chart")

df.groupby("Category")["Profit"].sum().plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()