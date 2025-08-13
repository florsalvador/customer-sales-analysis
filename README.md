# Customer Sales Analysis

## Overview
This project is a **Python and Pandas analysis of sales and customer data**.  
It reads sales from a CSV file and customer information from an Excel file, merges the data, performs various analyses, and exports results to CSV and Excel.

## Features
- Merge sales and customer data
- Compute total sales by:
  - City
  - Product
  - Customer
- Identify the best customer
- Filter sales by date range
- Filter customers by minimum total amount spent
- Export all analysis results:
  - Individual CSV files
  - Combined Excel file with multiple sheets

## Project Structure
```text

customer-sales-analysis/
├─ data/ # Input files
│ ├─ sales.csv
│ └─ customers.xlsx
├─ main.py # Main script
├─ analysis.py # Functions to analyze data
├─ utils.py # Functions for file export
└─ results/ # Output folder created automatically

```

## How to Run
1. Make sure you have Python 3.10+ installed.
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
3. Run the main script:
```bash
python main.py
```
4. Results will be exported to the results/ folder.
