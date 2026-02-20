"""
Módulo data_manager.py
Gestiona la persistencia de datos utilizando Pandas.
"""

import os
import pandas as pd


def cargar_dataframe(archivo, columnas):
    """
    Carga un DataFrame desde un CSV. Si no existe o está corrupto,
    crea uno nuevo con las columnas especificadas (Req 5).
    """
    if os.path.exists(archivo):
        try:
            return pd.read_csv(archivo)
        except (pd.errors.EmptyDataError, pd.errors.ParserError):
            print(f"Error: Datos invalidos en {archivo}. Creando uno nuevo.")
    
    return pd.DataFrame(columns=columnas)

def guardar_dataframe(df, archivo):
    """Guardar Dataframe en archivo CSV"""

    try:
        df.to_csv(archivo, index=False)
    except IOError as err:
        print(f"Error: Ocurrio un error al guardar los datos en {archivo}: {err}")
