import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import pearsonr
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

def baseline_model(df):

    # Dividir o dataset em treino (80%) e teste
    split_ratio = 0.8
    split_index = int(len(df) * split_ratio)
    df_train = df.iloc[:split_index]
    df_test = df.iloc[split_index:]

    # Criando uma cópia de df_test para realizar operações nele
    df_test = df_test.copy()

    # Usando as médias móveis para previsão. Aplicar shift para evitar data leak.
    df_test['predicted_qtd_7d'] = df_test.groupby('item')['ma_qtd_7d'].shift(1)
    df_test['predicted_qtd_14d'] = df_test.groupby('item')['ma_qtd_14d'].shift(1)

    # Remover linhas com valores NaN nas colunas de previsão
    df_test = df_test.dropna(subset=['predicted_qtd_7d', 'predicted_qtd_14d'])

    # Criando dataframe para armazenar as métricas
    metrics_df = pd.DataFrame(columns=['MAE', 'RMSE', 'MAPE'])

    # Função para calcular o MAPE
    def mean_absolute_percentage_error(y_true, y_pred):
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

    # Calculando métricas para as médias de 7 e 14 dias
    for ma_type in ['predicted_qtd_7d', 'predicted_qtd_14d']:
        y_true = df_test['qtd'].astype(float)
        y_pred = df_test[ma_type]
        
        # MAE
        mae = mean_absolute_error(y_true, y_pred)
        
        # RMSE
        mse = mean_squared_error(y_true, y_pred)
        rmse = np.sqrt(mse)
        
        # MAPE
        mape = mean_absolute_percentage_error(y_true, y_pred)
        
        # Armazena as métricas no dataframe, garantindo que elas sejam do tipo float
        metrics_df.loc[ma_type, 'MAE'] = np.round(float(mae), 4)
        metrics_df.loc[ma_type, 'RMSE'] = np.round(float(rmse), 4)
        metrics_df.loc[ma_type, 'MAPE'] = np.round(float(mape), 4)

    # Renomeando o índice
    metrics_df.rename(index={'predicted_qtd_7d': 'média 7 dias', 'predicted_qtd_14d': 'média 14 dias'}, inplace=True)

    # Exibe as métricas
    print(metrics_df)

    # Plotando o gráfico das previsões feitas pela melhor média móvel x valores 
    # Preparando grid
    plt.figure(figsize=(8, 4))
    sns.set_style('whitegrid')

    # Plotando qtd e data
    sns.lineplot(x='data', y='qtd', data=df_test, label='Actual', marker='o')

    # Plotando previsões para MA 7 dias
    # sns.lineplot(x='data', y='predicted_qtd_7d', data=df_test, label='7-day MA Forecast', marker='o')

    # Plotando previsões para MA 14 dias
    sns.lineplot(x='data', y='predicted_qtd_14d', data=df_test, label='14-day MA Forecast', marker='o')

    # Títulos e legendas
    plt.xlabel('Date')
    plt.ylabel('Quantity')
    plt.title('Actual vs Forecasted Quantity')

    # Rotacionando legendas do eixo x para melhor visualização
    plt.xticks(rotation=45)

    # Exibe a legenda do gráfico
    plt.legend()

    # Exibe o gráfico completo
    plt.tight_layout()
    plt.savefig('imagens/baseline.png') # em vez de exibir, salva a imagem
    # plt.show()


# Função para calcular o MAPE
def mean_absolute_percentage_error(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


def random_forest(df, data, features:list):
    # Ordenando df por data
    df = df.sort_values(by=data)

    # Particionando df
    split_ratio = 0.8  # 80% treino
    split_index = int(split_ratio * len(df))
    df_train = df.iloc[:split_index]
    df_test = df.iloc[split_index:]

    # Preparando X e y
    X_train = df_train[features]
    y_train = df_train['qtd']
    X_test = df_test[features]
    y_test = df_test['qtd']

    # Iniciando Random Forest
    rf_model = RandomForestRegressor(random_state=42)

    # Treinando o modelo
    rf_model.fit(X_train, y_train)

    # Previsões
    rf_pred = rf_model.predict(X_test)

    # Calculando métricas
    rf_mae = mean_absolute_error(y_test, rf_pred)
    rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
    rf_mape = mean_absolute_percentage_error(y_test, rf_pred)

    print(f"Métricas RF:")
    print(f"MAE: {rf_mae:.2f}")
    print(f"RMSE: {rf_rmse:.2f}")
    print(f"MAPE: {rf_mape:.2f}")

    # Plotando previsões
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=df_test['data'], y=y_test, label='Atual', color='blue')
    sns.lineplot(x=df_test['data'], y=rf_pred, label='Previsão RF', color='green')
    plt.xlabel('Data')
    plt.ylabel('Quantidade vendida')
    plt.title('Quantidade vendida x prevista (random forest)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('imagens/random_forest.png') # em vez de exibir, salva a imagem
    # plt.show()

def xgboost(df, data, features:list):
    # Ordenando df por data
    df = df.sort_values(by=data)

    # Particionando df
    split_ratio = 0.8  # 80% treino
    split_index = int(split_ratio * len(df))
    df_train = df.iloc[:split_index]
    df_test = df.iloc[split_index:]

    # Preparando X e y
    X_train = df_train[features]
    y_train = df_train['qtd']
    X_test = df_test[features]
    y_test = df_test['qtd']

    # Inicializando modelo
    xgb_model = XGBRegressor(random_state=42)
    xgb_model.fit(X_train, y_train)

    # Previsões
    xgb_pred = xgb_model.predict(X_test)

    # Cálculo das métricas
    xgb_mae = mean_absolute_error(y_test, xgb_pred)
    xgb_rmse = np.sqrt(mean_squared_error(y_test, xgb_pred))
    xgb_mape = mean_absolute_percentage_error(y_test, xgb_pred)

    print(f"XGBoost Metrics:")
    print(f"MAE: {xgb_mae:.2f}")
    print(f"RMSE: {xgb_rmse:.2f}")
    print(f"MAPE: {xgb_mape:.2f}")

    # Plotando
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=df_test['data'], y=y_test, label='Atual', color='blue')
    sns.lineplot(x=df_test['data'], y=xgb_pred, label='Previsão XGB', color='red')
    plt.xlabel('Data')
    plt.ylabel('Quantidade vendida')
    plt.title('Quantidade vendida x prevista (xgb)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('imagens/xgboost.png') # em vez de exibir, salva a imagem
    # plt.show()