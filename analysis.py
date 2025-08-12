import pandas as pd

def merge_data(sales: pd.DataFrame, customers: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(sales, customers, on="customer_id")
    df["total_amount"] = df["price"] * df["quantity"]
    df["date"] = pd.to_datetime(df["date"])
    return df

def sales_grouped_by(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    grouped = (
        df.groupby(columns, as_index=False)["total_amount"].sum()
        .sort_values("total_amount", ascending=False)
        )
    return grouped

def sales_by_city(df: pd.DataFrame) -> pd.DataFrame:
    return sales_grouped_by(df, ["city"])

def sales_by_product(df: pd.DataFrame) -> pd.DataFrame:
    return sales_grouped_by(df, ["product"])

def sales_by_customer(df: pd.DataFrame) -> pd.DataFrame:
    return sales_grouped_by(df, ["customer_id", "name"])

def get_best_customer(df: pd.DataFrame) -> pd.DataFrame:
    grouped = sales_by_customer(df)
    result = grouped[["name"]].head(1).rename(columns={"name": "best_customer"})
    return result

def get_sales_by_dates(df: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    result = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    return result

def get_customers_by_min_amount(df: pd.DataFrame, amount: int) -> pd.DataFrame:
    grouped = sales_by_customer(df)
    result = grouped[grouped["total_amount"] >= amount]
    return result
