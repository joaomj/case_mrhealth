import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analise_descritiva(df):

    # informações gerais da tabela: nomes de colunas, tamanho, tipos de dados
    print('\nInformações gerais do dataset:')
    df.info()

    # quantidade de valores únicos
    print('\nQuantidade de valores únicos:')
    df.nunique()

    # estatísticas descritivas da tabela
    print('Estatísticas descritivas:')
    df[['item', 'qtd', 'vlr_unitario', 'vlr_total']].groupby('item').describe().round(2).T


def boxplot_dia(df):
    # Boxplot agregando dados diários

    # Definindo cores para cada item
    colors = {'A': 'blue', 'B': 'green', 'C': 'red', 'D': 'purple'}

    # Gerar boxplots
    plt.figure(figsize=(6, 4)) 

    # Criando boxplots com a paleta customizada
    sns.boxplot(data=df, x='item', y='qtd', hue='item', palette=colors, order=['A', 'B', 'C', 'D'], legend=False)

    # Título e labels
    plt.xlabel('Item')
    plt.ylabel('Quantidade')
    plt.title('Boxplot da Quantidade Vendida de Cada Item por Dia')

    plt.tight_layout()
    plt.savefig('imagens/boxplot_dia.png') # em vez de exibir, salva a imagem
    # plt.show()

def boxplot_semana(df):
    # Boxplot agregando dados semanais
    df_weekly_agg = df.groupby(['item', 'semana'], as_index=False, observed=False)['qtd'].sum()

    # Plotando
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=df_weekly_agg, x='item', y='qtd', hue='item', palette='husl', legend=False)
    plt.xlabel('Item')
    plt.ylabel('Quantidade')
    plt.title('Distribuição da Quantidade Semanal por Item')
    plt.savefig('imagens/boxplot_semana.png') # em vez de exibir, salva a imagem
    # plt.show()

def boxplot_mes(df):
    # # Boxplot agregando dados mensais
    df_monthly_agg = df.groupby(['item', 'mes'], as_index=False, observed=False)['qtd'].sum()

    # Plotando
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=df_monthly_agg, x='item', y='qtd', hue='item', palette='husl', legend=False)
    plt.xlabel('Item')
    plt.ylabel('Quantidade')
    plt.title('Distribuição da Quantidade Mensal por Item')
    plt.savefig('imagens/boxplot_mes.png') # em vez de exibir, salva a imagem
    # plt.show()