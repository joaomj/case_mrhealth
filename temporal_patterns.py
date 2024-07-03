import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import warnings

# Silence all UserWarning messages
warnings.filterwarnings("ignore", category=UserWarning)


def qtd_por_dia(df):
    # Gráfico de Série Temporal: 'qtd' no tempo

    # Cores distintas para items A, B, C, D
    palette = {'A': 'blue', 'B': 'orange', 'C': 'green', 'D': 'red'}

    # Ordem das colunas no gráfico
    col_order = ['A', 'B', 'C', 'D']

    # FacetGrid com Seaborn
    sns.set_theme(style="whitegrid")
    g = sns.FacetGrid(df, col="item", col_wrap=2, col_order=col_order, height=5, aspect=1.5, palette=palette.keys(), despine=True)
    g.map_dataframe(sns.lineplot, x='data', y='qtd', hue='item', palette=palette, marker='o', markersize=8)
    g.set_axis_labels("Date", "Quantity")
    g.set_titles("Item {col_name}")
    g.tight_layout()
    g.add_legend()

    # Rotacionando os labels do eixo x
    for ax in g.axes.flatten():  # percorre todos os eixos
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)  # rotaciona labels

    # plt.show()
    plt.savefig('imagens/qtd_dia.png') # em vez de exibir, salva a imagem

def qtd_semana (df):
    # Quantidade por semana

    # Agrupar por semana e por item
    df_weekly = df.groupby(['item', 'semana'])['qtd'].sum().reset_index()

    # Plotar com Seaborn
    plt.figure(figsize=(8, 4))
    sns.set_theme(style="whitegrid")
    sns.lineplot(data=df_weekly, x='semana', y='qtd', hue='item', marker='o', palette="husl")

    plt.xlabel('Semana do Ano')
    plt.ylabel('Quantidade')
    plt.title('Quantidade Vendida por Item por Semana')
    plt.legend(title='Item')
    plt.xticks(df_weekly['semana'].unique())

    #plt.show()
    plt.savefig('imagens/qtd_semana.png') # em vez de exibir, salva a imagem

def qtd_mes (df):
    # Quantidade por mês

    # Agrupar por mês e por item
    df_monthly = df.groupby(['item', 'mes'])['qtd'].sum().reset_index()

    # Plotar com Seaborn
    plt.figure(figsize=(8, 4))
    sns.set_theme(style="whitegrid")
    sns.lineplot(data=df_monthly, x='mes', y='qtd', hue='item', marker='o', palette="husl")

    plt.xlabel('Mês')
    plt.ylabel('Quantidade')
    plt.title('Quantidade Vendida por Item por Mês')
    plt.legend(title='Item')
    plt.xticks(df_monthly['mes'].unique())

    # plt.show()
    plt.savefig('imagens/qtd_mes.png') # em vez de exibir, salva a imagem
