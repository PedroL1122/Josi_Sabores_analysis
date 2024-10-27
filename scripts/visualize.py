import matplotlib.pyplot as plt

def plot_monthly_sales(monthly_sales):
    monthly_sales.plot(kind='bar')
    plt.title('Vendas Mensais')
    plt.xlabel('Mês')
    plt.ylabel('Quantidade Vendida')
    plt.show()

def plot_top_products(top_products):
    top_products.plot(kind='bar', color='orange')
    plt.title('Top Produtos Vendidos')
    plt.xlabel('Produto')
    plt.ylabel('Quantidade Vendida')
    plt.show()
