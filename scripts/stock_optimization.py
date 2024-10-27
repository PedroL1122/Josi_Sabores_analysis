import pandas as pd

def stock_needs(sales_data, stock_data):
    future_demand = sales_data.groupby('produto').mean()['quantidade'] * 4  # previsão para os próximos 4 meses
    stock_needs = future_demand - stock_data.set_index('produto')['quantidade']
    stock_needs[stock_needs < 0] = 0  # zerar valores negativos
    return stock_needs
