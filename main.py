import pandas as pd
from analysis import (
    merge_data, sales_by_city, sales_by_customer, sales_by_product, 
    get_best_customer, get_sales_by_dates, get_customers_by_min_amount
)
from pathlib import Path

def create_folder():
    cwd = Path.cwd()
    path_folder = cwd / "results"
    path_folder.mkdir(exist_ok=True)
    return path_folder

sales = pd.read_csv("data/sales.csv")
customers = pd.read_excel("data/customers.xlsx")

df = merge_data(sales, customers)

def save_as_csv(df: pd.DataFrame, filename: str):
    path = create_folder() / filename
    df.to_csv(path, index=False)
    print(f"File {filename} created:", path)

df_sales_by_city = sales_by_city(df)
df_sales_by_product = sales_by_product(df)
df_sales_by_customer = sales_by_customer(df)
df_best_customer = get_best_customer(df)
df_sales_between_dates = get_sales_by_dates(df, "2025-01-15", "2025-01-25")
df_customers_min_amount = get_customers_by_min_amount(df, 100)

print("Saving analysis into csv files")
save_as_csv(df_sales_by_city, "sales_by_city.csv")
save_as_csv(df_sales_by_product, "sales_by_product.csv")
save_as_csv(df_sales_by_customer, "sales_by_customer.csv")
save_as_csv(df_best_customer, "best_customer.csv")
save_as_csv(df_sales_between_dates, "sales_between_dates.csv")
save_as_csv(df_customers_min_amount, "customers_min_amount.csv")

def save_as_xlsx(dataframes: list[pd.DataFrame], sheet_names: list[str], filename: str):
    path = create_folder() / filename
    with pd.ExcelWriter(path) as writer:
        for i in range(len(dataframes)):
            dataframes[i].to_excel(writer, sheet_name=sheet_names[i], index=False)
    print(f"File {filename} created:", path)

dataframes = [
    df_sales_by_city,
    df_sales_by_product,
    df_sales_by_customer,
    df_best_customer,
    df_sales_between_dates,
    df_customers_min_amount
]

sheet_names = [
    "sales_by_city", 
    "sales_by_product", 
    "sales_by_customer", 
    "best_customer", 
    "sales_between_dates", 
    "customers_min_amount"
    ]

print("Saving analysis into excel file")
save_as_xlsx(dataframes, sheet_names, "analysis.xlsx")
