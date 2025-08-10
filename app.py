import pandas as pd

sales = pd.read_csv("data/sales.csv")
customers = pd.read_excel("data/customers.xlsx")

df = pd.merge(sales, customers, on="customer_id")
df["total_amount"] = df["price"] * df["quantity"]

print(df)
