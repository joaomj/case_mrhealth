import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings
# instalar openpyxl para leitura dos arquivos excel (https://stackoverflow.com/a/56992903)

from data_io import io_data
from data_preparation import consolidate_data
from feature_engineering import feature_engineering
from exploratory_analysis import analise_descritiva, boxplot_dia, boxplot_semana, boxplot_mes
from business_questions import maior_demanda_dia, maior_demanda_item, maior_demanda_mes, preco_demanda, pedido_medio
from temporal_patterns import qtd_por_dia, qtd_semana, qtd_mes
from modelling import baseline_model, random_forest, xgboost

if __name__ == "__main__":
    # Lendo arquivos de dados

    # Obtendo o path deste notebook
    current_dir = os.getcwd()

    # Construindo o path para os arquivos excel
    itens_path = os.path.join(current_dir, 'dados', 'itens.xlsx')
    pedido_path = os.path.join(current_dir, 'dados', 'pedido.xlsx')
    itens_pedido_path = os.path.join(current_dir, 'dados', 'itens_pedido.xlsx')

    # obtendo arquivos
    df_itens = io_data(itens_path, 'r')
    df_pedido = io_data(pedido_path, 'r')
    df_itens_pedido = io_data(itens_pedido_path, 'r')

    # consolidando dados
    df = consolidate_data(df_itens, df_pedido, df_itens_pedido)

    # feature engineering
    df1 = feature_engineering(df)

    # salvar dataframe preparado
    current_dir = os.getcwd()
    path = os.path.join(current_dir, 'dados', 'df1.csv')
    io_data(path, 'w', df1)

    # análise exploratória
    analise_descritiva(df1)
    boxplot_dia(df1)
    boxplot_semana(df1)
    boxplot_mes(df1)

    # padrões temporais
    qtd_por_dia(df1)
    qtd_semana(df1)
    qtd_mes(df1)

    # perguntas de negócio
    maior_demanda_dia(df1)
    maior_demanda_mes(df1)
    maior_demanda_item(df1)
    preco_demanda(df1)
    pedido_medio(df1)

    # features
    features = ['vlr_unitario',
        'mes',
        'dia',
        'dia_semana',
        'semana',
        'trimestre',
        'fim_de_semana',
        'sen_dia_semana',
        'cos_dia_semana',
        'sen_semana',
        'cos_semana',
        'sen_trimestre',
        'cos_trimestre',
        'ma_qtd_7d',
        'ma_qtd_14d',
        'lag_7',
        'lag_14']


    # modelagem
    baseline_model(df1)
    random_forest(df1, 'data', features)
    xgboost(df1, 'data', features)








