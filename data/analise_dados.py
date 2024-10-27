import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv("C:/Users/peque/OneDrive/Documentos/doce_delicia_analysis/data/sales_data.csv")


# Carregar os dados de vendas e estoque
vendas_df = pd.read_csv('data/sales_data.csv')
estoque_df = pd.read_csv('data/stock_data.csv')

# Análise básica das vendas
def resumo_vendas():
    print("Resumo das Vendas:")
    print(vendas_df.describe())
    print("\n")

# Análise básica do estoque
def resumo_estoque():
    print("Resumo do Estoque:")
    print(estoque_df.describe())
    print("\n")

# Identificar produtos com estoque crítico (menor que 5 unidades)
def estoque_critico():
    estoque_critico_df = estoque_df[estoque_df['quantidade'] < 5]
    if estoque_critico_df.empty:
        print("Não há produtos com estoque crítico.\n")
    else:
        print("Produtos com Estoque Crítico:")
        print(estoque_critico_df[['produto', 'quantidade']])
        print("\n")

# Gráfico de vendas por produto
def grafico_vendas():
    vendas_totais = vendas_df.groupby('produto')['quantidade'].sum()
    vendas_totais.plot(kind='bar', color='skyblue')
    plt.title("Vendas Totais por Produto")
    plt.xlabel("Produto")
    plt.ylabel("Quantidade Vendida")
    plt.show()

# Gráfico de estoque atual por produto
def grafico_estoque():
    estoque_df.plot(x='produto', y='quantidade', kind='bar', color='salmon')
    plt.title("Estoque Atual por Produto")
    plt.xlabel("Produto")
    plt.ylabel("Quantidade em Estoque")
    plt.show()

# Chamada das funções de análise
if __name__ == "__main__":
    # Exibir resumo das vendas e estoque
    resumo_vendas()
    resumo_estoque()
    
    # Exibir produtos com estoque crítico
    estoque_critico()
    
    # Exibir gráficos de vendas e estoque
    grafico_vendas()
    grafico_estoque()
