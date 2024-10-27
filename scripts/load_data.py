import pandas as pd

def load_sales_data(file_path):
    sales_data = pd.read_csv(file_path, parse_dates=['data'])
    return sales_data

def load_stock_data(file_path):
    stock_data = pd.read_csv(file_path)
    return stock_data
