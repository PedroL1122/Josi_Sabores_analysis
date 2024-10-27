from scripts.load_data import load_sales_data, load_stock_data
from scripts.sales_analysis import monthly_sales_summary, top_products
from scripts.stock_optimization import stock_needs
from scripts.visualize import plot_monthly_sales, plot_top_products

# Carregar dados
sales_data = load_sales_data('data/sales_data.csv')
stock_data = load_stock_data('data/stock_data.csv')

# Análise de Vendas
monthly_sales = monthly_sales_summary(sales_data)
top_products_list = top_products(sales_data)

# Otimização de Estoque
stock_needs_report = stock_needs(sales_data, stock_data)

# Visualização
plot_monthly_sales(monthly_sales)
plot_top_products(top_products_list)

# Resultados
print("Necessidade de Estoque (próximos 4 meses):\n", stock_needs_report)
