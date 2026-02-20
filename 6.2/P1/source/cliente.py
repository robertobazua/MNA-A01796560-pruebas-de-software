"""Modulo Cliente.py"""

import pandas as pd
from data_manager import cargar_dataframe, guardar_dataframe

ARCHIVO = "bd_clientes.csv"
COLUMNAS = ["id", "nombre", "email"]

class Cliente:
    """Clase Cliente"""

    @classmethod
    def crear_cliente(cls, id, nombre, email):
        
        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        
        if id in df["id"].values:
            print(f"Error: ID {id} ya existe.")
            return False
        
        nuevo_reg = pd.DataFrame([[id, nombre, email]], columns=COLUMNAS)
        df = pd.concat(df[df, nuevo_reg], ignore_index=True)
        guardar_dataframe(df, ARCHIVO)
        return True
    
    