import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import holidays
import matplotlib.dates as mdates
import warnings


def feature_engineering(df):

    # Extraindo dia, mês e ano da data
    df['ano'] = df['data'].dt.year
    df['mes'] = df['data'].dt.month
    df['dia'] = df['data'].dt.day

    # Extraindo dia da semana e nome do dia
    df['dia_semana'] = df['data'].dt.dayofweek # monday/segunda = 0
    df['nome_dia'] = df['data'].dt.day_name()

    # Traduzir nomes dos dias
    nome_dia_traduzido = {
    'Monday': 'segunda-feira',
    'Tuesday': 'terça-feira',
    'Wednesday': 'quarta-feira',
    'Thursday': 'quinta-feira',
    'Friday': 'sexta-feira',
    'Saturday': 'sábado',
    'Sunday': 'domingo'
    }

    df['nome_dia'] = df['nome_dia'].replace(nome_dia_traduzido)

    # Extraindo semana do ano, trimestre do ano
    df['semana'] = df['data'].dt.isocalendar().week
    df['trimestre'] = df['data'].dt.quarter

    # é fim de semana?
    df['fim_de_semana'] = (df['data'].dt.dayofweek > 4).astype(int) # se dia da semana > 4 (sexta = 4), então é weekend. Converte booleano p/int

    # é feriado?
    feriados = holidays.Brazil()
    df['feriado'] = df['data'].isin(feriados).astype(int)

    # cíclicas
    # Como a empresa não funciona em feriados, existe ciclicidade na demanda. Logo, é útil transformar dados para suavizar os ciclos.
    # Vamos transformar: dia_semana, semana e trimestre porque são cíclicos no tempo
    df['sen_dia_semana'] = np.sin(2 * np.pi * df['dia_semana']/7)
    df['cos_dia_semana'] = np.cos(2 * np.pi * df['dia_semana']/7)

    df['sen_semana'] = np.sin(2 * np.pi * df['semana']/52)
    df['cos_semana'] = np.cos(2 * np.pi * df['semana']/52)

    df['sen_trimestre'] = np.sin(2 * np.pi * df['trimestre']/4)
    df['cos_trimestre'] = np.cos(2 * np.pi * df['trimestre']/4)


    # verifica se não trabalha em feriados (soma vai dar zero)
    if df['feriado'].sum() > 0:
        print('Trabalha em feriados')
    else:
        print('Não trabalha em feriados')

    # verifica se não trabalha em finais de semana (soma vai dar zero)
    if df['fim_de_semana'].sum() > 0:
        print('Trabalha em fds')
    else:
        ('Não trabalha em fds')

    # Calcula médias móveis para cada item com períodos de 7 e 14 dias.
    window_sizes = [7, 14]  # período em dias
    for window in window_sizes:
        df[f'ma_qtd_{window}d'] = df.groupby('item')['qtd'].rolling(window=window, min_periods=1).mean().reset_index(drop=True)
    
    # Calcula lags de 7 e 14 dias da qtd
    df['lag_7'] = df['qtd'].shift(7)  # Mostra o valor de qtd 7 dias atrás
    df['lag_14'] = df['qtd'].shift(14)  # Mostra o valor de qtd 14 dias atrás

    # Exclui linhas com valores nulos
    df.dropna(subset=['lag_7', 'lag_14'], inplace=True)

    # Deletando colunas irrelevantes
    # coluna 'ano' porque os dados estão todos no mesmo ano ('2021')
    # coluna 'feriado' porque a empresa nunca funciona em feriados
    df = df.drop(columns=['feriado', 'ano'])

    return df