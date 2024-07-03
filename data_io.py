import os
import pandas as pd
# instalar openpyxl para leitura dos arquivos excel (https://stackoverflow.com/a/56992903)

def io_data(path, operation:str, df=None):
    
    if operation == 'r':
        # Importando arquivos excel como dataframes
        df = pd.read_excel(path)
        return df
    
    elif operation == 'w':
        # Salvando em csv
        df.to_csv(path, index=False)
        return 'Dados salvos!'
    
    else:
        raise ValueError("Operação inválida. Use 'r' para carregar ou 'w' para salvar o dataset.")
