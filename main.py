import pandas as pd
from analysis import (
    merge_data, sales_by_city, sales_by_customer, sales_by_product, 
    get_best_customer, get_sales_by_dates, get_customers_by_min_amount
)

sales = pd.read_csv("data/sales.csv")
customers = pd.read_excel("data/customers.xlsx")

df = merge_data(sales, customers)

print("Sales by city:\n", sales_by_city(df))
print("Sales by product:\n", sales_by_product(df))
print("Sales by customer:\n", sales_by_customer(df))
print("Best customer:\n", get_best_customer(df))
print("Get sales between dates:\n", get_sales_by_dates(df, "2025-01-15", "2025-01-25"))
print("Customers who spent at least 100 dollars:\n", get_customers_by_min_amount(df, 100))
