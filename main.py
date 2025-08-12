import pandas as pd

sales = pd.read_csv("data/sales.csv")
customers = pd.read_excel("data/customers.xlsx")

df = pd.merge(sales, customers, on="customer_id")
df["total_amount"] = df["price"] * df["quantity"]
df["date"] = pd.to_datetime(df["date"])
print("Sales and customers data merged:\n", df)

sales_by_city = (
    df.groupby("city", as_index=False)["total_amount"].sum()
    .sort_values("total_amount", ascending=False)
    )
print("Sales by city:\n", sales_by_city)

sales_by_product = (
    df.groupby("product", as_index=False)["total_amount"].sum()
    .sort_values("total_amount", ascending=False)
    )
print("Sales by product:\n", sales_by_product)

sales_by_customer = (
    df.groupby(["customer_id", "name"], as_index=False)["total_amount"].sum()
    .sort_values("total_amount", ascending=False)
    )
print("Sales by customer:\n", sales_by_customer)

best_customer = sales_by_customer[["name"]].head(1).rename(columns={"name": "best_customer"})
print("Best customer:\n", best_customer)

def get_sales_by_date(df: pd.DataFrame, start_date: str, end_date: str):
    result = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    return result

print("Get sales between dates:\n", get_sales_by_date(df, "2025-01-15", "2025-01-25"))

def get_customers_by_min_amount(df: pd.DataFrame, amount: int):
    filtered = df.groupby(["customer_id", "name"], as_index=False)["total_amount"].sum()
    result = filtered[filtered["total_amount"] >= amount]
    return result

print("Customers who spent at least x dollars:\n", get_customers_by_min_amount(df, 100))
