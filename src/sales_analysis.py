import pandas as pd
import matplotlib.pyplot as plt

print("=" * 50)
print("SALES ANALYSIS PROJECT")
print("=" * 50)

df = pd.read_excel("data/Sample - Superstore.xls")

print("\nDataset Loaded Successfully")
print(df.head())

# --------------------- CATEGORY SALES ---------------------

category_sales = df.groupby("Category")["Sales"].sum()

print("\nCategory-wise Sales")
print(category_sales)

plt.figure(figsize=(8, 5))
category_sales.plot(
    kind="bar",
    color=["royalblue", "seagreen", "darkorange"]
)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("outputs/charts/category_sales.png")
plt.show()

# --------------------- CATEGORY PROFIT ---------------------

category_profit = df.groupby("Category")["Profit"].sum()

print("\nCategory-wise Profit")
print(category_profit)

plt.figure(figsize=(8, 5))
category_profit.plot(
    kind="bar",
    color=["purple", "crimson", "teal"]
)
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("outputs/charts/category_profit.png")
plt.show()

# --------------------- REGION SALES ---------------------

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(7, 7))
region_sales.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Regional Sales Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("outputs/charts/region_sales.png")
plt.show()

# --------------------- CUSTOMER SEGMENT ---------------------

segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(8, 5))
segment_sales.plot(
    kind="bar",
    color=["gold", "skyblue", "lightgreen"]
)
plt.title("Sales by Customer Segment")
plt.xlabel("Segment")
plt.ylabel("Sales")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("outputs/charts/segment_sales.png")
plt.show()

# --------------------- TOP PRODUCTS ---------------------

top_products = (
    df.groupby("Product Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop 10 Products by Sales")
print(top_products)

plt.figure(figsize=(10, 6))
plt.barh(
    top_products.index,
    top_products.values,
    color="teal"
)
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/charts/top_products.png")
plt.show()

# --------------------- MONTHLY SALES ---------------------

df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
      .sum()
)

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(12, 5))
plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    linewidth=2,
    color="blue"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/charts/monthly_sales.png")
plt.show()

# --------------------- TOP CUSTOMERS ---------------------

top_customers = (
    df.groupby("Customer Name")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop 10 Customers")
print(top_customers)

plt.figure(figsize=(11, 6))
plt.barh(
    top_customers.index,
    top_customers.values,
    color="darkorange"
)
plt.title("Top 10 Customers by Sales")
plt.xlabel("Sales")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/charts/top_customers.png")
plt.show()

# --------------------- DISCOUNT VS PROFIT ---------------------

plt.figure(figsize=(10, 6))
plt.scatter(
    df["Discount"],
    df["Profit"],
    color="red",
    alpha=0.5
)
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/charts/discount_vs_profit.png")
plt.show()

print("\n" + "=" * 50)
print("Sales Analysis Completed Successfully")
print("Charts have been saved in outputs/charts/")
print("=" * 50)