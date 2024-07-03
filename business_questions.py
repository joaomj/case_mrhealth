import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def maior_demanda_mes(df):
    # Encontrando o mês de maior e menor demanda para cada item
    # Este código agrupa o dataframe por item e mês, ordena por item e qtd e exibe a primeira linha (maior/menor demanda)

    # Agrupando por item e mês, somando a qtd
    demanda_mes = df.groupby(['item', 'mes'])['qtd'].sum().reset_index()

    # Maior demanda
    maior_demanda_mes = demanda_mes.sort_values(['item', 'qtd'], ascending=[True, False]).groupby('item').head(1)
    print('Mês com maior demanda para cada item:')
    print(maior_demanda_mes)

    # Menor demanda
    menor_demanda_mes = demanda_mes.sort_values(['item', 'qtd'], ascending=[True, True]).groupby('item').head(1)
    print('\nMês com menor demanda para cada item:')
    print(menor_demanda_mes)

def maior_demanda_dia(df):
    # Agrupando por item e dia da semana, calculando a média da qtd
    demanda_dia_semana = df.groupby(['item', 'nome_dia'])['qtd'].mean().round(2).reset_index()

    # Maior demanda média
    print('Dia da semana com maior demanda média para cada item:')
    print(demanda_dia_semana.sort_values(['item', 'qtd'], ascending=[True, False]).groupby('item').head(1))

    # Menor demanda média
    print('\nDia da semana com menor demanda média para cada item:')
    print(demanda_dia_semana.sort_values(['item', 'qtd'], ascending=[True, False]).groupby('item').tail(1))

def maior_demanda_item(df):
    # Agrupando por item e somando a qtd
    demanda_total = df.groupby(['item'])['qtd'].sum().reset_index()

    # Ordenando a demanda em ordem decrescente
    demanda_total = demanda_total.sort_values('qtd', ascending=False)

    print('O item com maior demanda no período foi:')
    print(demanda_total.head(1))

    print('\nO item com menor demanda no período foi:')
    print(demanda_total.tail(1))

def preco_demanda(df):
    # Agrupando por quantidade e preço médio de cada item
    item_summary = df.groupby('item').agg({
        'qtd': 'sum',             
        'vlr_unitario': 'mean'    
    }).reset_index()

    # Calculando correlação
    correlation = item_summary['qtd'].corr(item_summary['vlr_unitario'])

    print(f"Correlação entre qtd_sold e vlr_unitario: {correlation:.4f}")

    # Filtrando o outlier item 'D'
    item_summary_filtered = item_summary[item_summary['item'] != 'D']

    # Calculando correlação
    correlation = item_summary_filtered['qtd'].corr(item_summary_filtered['vlr_unitario'])

    print(f"Correlação entre qtd_sold e vlr_unitario (sem item D): {correlation:.4f}")

   
    # Plotando gráfico de qtd x preço de cada item, para avaliar linearidade
    # Preparando gráfico
    plt.figure(figsize=(8, 4))
    plt.scatter(item_summary['vlr_unitario'], item_summary['qtd'], marker='o', color='b')

    # Labels e título
    plt.xlabel('Preço do Item (vlr_unitario)')
    plt.ylabel('Quantidade Vendida (qtd)')
    # plt.title('Scatter Plot of Item Price vs. Quantity Sold')

    # Adicionando o nome de cada ítem
    for i, txt in enumerate(item_summary['item']):
        plt.annotate(txt, (item_summary['vlr_unitario'][i], item_summary['qtd'][i]), fontsize=12)

    plt.grid(True)
    plt.savefig('imagens/correlacoes.png') # em vez de exibir, salva a imagem
    # plt.show()

def pedido_medio(df):
    # Média da quantidade de itens por pedido
    print('Quantidade média de itens por pedido:')
    print(df.groupby('pedido')['qtd'].sum().mean().round(2))

    # Valor médio dos pedidos
    print('\nValor médio dos pedidos:')
    print(df.groupby('pedido')['vlr_total'].sum().mean().round(2))

    # Qual a quantidade média de cada item em um pedido típico?
    avg_itens = df.groupby(['item'])['qtd'].mean().round().reset_index()
    avg_itens.columns = ['item', 'qtd_média_por_ordem']
    print('\nQuantidade média de cada item em um pedido típico:')
    print(avg_itens)