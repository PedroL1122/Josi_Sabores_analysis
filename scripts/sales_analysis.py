import pandas as pd

def monthly_sales_summary(sales_data):
    sales_data['mes'] = sales_data['data'].dt.to_period('M')
    monthly_sales = sales_data.groupby('mes').sum()['quantidade']
    return monthly_sales

def top_products(sales_data, top_n=5):
    product_sales = sales_data.groupby('produto').sum()['quantidade']
    return product_sales.nlargest(top_n)
