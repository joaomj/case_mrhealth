# Consolida todos os dados em um único dataframe

import pandas as pd

def consolidate_data(df_itens, df_pedido, df_itens_pedido):
    
    # renomear colunas de df_itens
    df_itens = df_itens.rename(columns={
        'Unnamed: 0': 'ID_ITEM',
        0: 'PRECO_ITEM'
    })

    # descartar colunas Unnamed de df_pedido e df_itens_pedido
    df_pedido = df_pedido.drop(columns='Unnamed: 0')
    df_itens_pedido = df_itens_pedido.drop(columns='Unnamed: 0')

    # adicionar 'PRECO_ITEM' na tabela 'df_itens_pedido' utilizando a tabela 'df_itens'
    df_itens_pedido = df_itens_pedido.merge(df_itens, on='ID_ITEM')

    # adicionar 'PRECO_TOTAL_ITEM' em 'df_itens_pedido'
    df_itens_pedido['PRECO_TOTAL_ITEM'] = df_itens_pedido['QUANTIDADE'] * df_itens_pedido['PRECO_ITEM']

    # adicionar coluna 'DATA' em 'df_itens_pedido' utilizando 'df_pedido'
    df_itens_pedido = df_itens_pedido.merge(df_pedido, on='ID_PEDIDO')
    df_itens_pedido = df_itens_pedido.drop(columns='VALOR_TOTAL')

    # converter formato da coluna 'DATA'
    df_itens_pedido['DATA'] = pd.to_datetime(df_itens_pedido['DATA'], format='%Y-%m-%d')
    df_itens_pedido.dtypes

    # Como a tabela principal é esta, vamos simplificar o nome
    df = df_itens_pedido

    # Mudar os nomes de colunas para letra minúscula
    df.columns = df.columns.str.lower()

    # Retirar a palavra 'item' de cada linha da coluna 'id_item'
    df['id_item'] = df['id_item'].str.replace('item ', '', case=False)

    # Mudar os nomes das colunas
    df.columns = ['pedido', 'item', 'qtd', 'vlr_unitario', 'vlr_total', 'data']

    return df