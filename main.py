import pandas as pd
from analysis import (
    merge_data, sales_by_city, sales_by_customer, sales_by_product, 
    get_best_customer, get_sales_by_dates, get_customers_by_min_amount
)
from utils import save_as_csv, save_as_xlsx


def main():
    sales = pd.read_csv("data/sales.csv")
    customers = pd.read_excel("data/customers.xlsx")
    df = merge_data(sales, customers)

    start_date = input("Enter start date (YYYY-MM-DD) or leave empty for default: ") or "2025-01-15"
    end_date = input("Enter end date (YYYY-MM-DD) or leave empty for default: ") or "2025-01-25"
    min_amount_input = input("Enter minimum customer spending or leave empty for default: ")
    try:
        min_amount = int(min_amount_input) if min_amount_input else 100
    except ValueError:
        print("Invalid input. Using default 100.")
        min_amount = 100

    analysis_results = {
        "sales_by_city": sales_by_city(df),
        "sales_by_product": sales_by_product(df),
        "sales_by_customer": sales_by_customer(df),
        "best_customer": get_best_customer(df),
        "sales_between_dates": get_sales_by_dates(df, start_date, end_date),
        "customers_min_amount": get_customers_by_min_amount(df, min_amount)
    }

    print("Saving analysis into CSV files...")
    for filename, df_result in analysis_results.items():
        save_as_csv(df_result, f"{filename}.csv")

    print("Saving analysis into Excel file...")
    save_as_xlsx(list(analysis_results.values()), list(analysis_results.keys()), "analysis.xlsx")


if __name__ == "__main__":
    main()
