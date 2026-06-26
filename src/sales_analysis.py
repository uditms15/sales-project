import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    return pd.read_excel("data/Sample - Superstore.xls")

def sales_by_category(df):
    return df.groupby("Category")["Sales"].sum()

def profit_by_category(df):
    return df.groupby("Category")["Profit"].sum()

def monthly_sales(df):
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    data = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
    data.index = data.index.astype(str)
    return data

def top_customers(df):
    return df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)

def plot_bar(data, title, color, filename):
    plt.figure(figsize=(8,5))
    data.plot(kind="bar", color=color)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(axis="y")
    plt.tight_layout()
    plt.savefig(f"outputs/charts/{filename}")
    plt.close()

def plot_line(data, title, filename):
    plt.figure(figsize=(10,5))
    plt.plot(data.index, data.values, marker="o")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"outputs/charts/{filename}")
    plt.close()

def main():
    print("Sales Project Started")

    df = load_data()
    print(df.head())

    cat_sales = sales_by_category(df)
    cat_profit = profit_by_category(df)
    month_sales = monthly_sales(df)
    customers = top_customers(df)

    plot_bar(cat_sales, "Sales by Category", "blue", "category_sales.png")
    plot_bar(cat_profit, "Profit by Category", "green", "category_profit.png")

    plot_line(month_sales, "Monthly Sales Trend", "monthly_sales.png")

    plot_bar(customers, "Top Customers", "orange", "top_customers.png")

    print("Project Completed Successfully")

if __name__ == "__main__":
    main()