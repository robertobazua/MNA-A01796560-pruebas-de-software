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
            print(f"Error: Cliente {id} ya existe.")
            return False
        nuevo_reg = pd.DataFrame([[id, nombre, email]], columns=COLUMNAS)
        df = pd.concat([df, nuevo_reg], ignore_index=True)
        guardar_dataframe(df, ARCHIVO)
        return True

    @classmethod
    def eliminar_cliente(cls, id):
        """Elimina un cliente por ID"""
        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        if id not in df["id"].values:
            print(f"Error: Cliente {id} no encontrado.")
            return False
        df = df[df["id"] != id]
        guardar_dataframe(df, ARCHIVO)
        return True

    @classmethod
    def listar_clientes(cls):
        """Lista todos los clientes"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        row = df[df["id"] == id]

        if row.empty:
            print(f"Error: Cliente {id} no encontrado.")
            return False
        print(row.to_string(index=False))
        return row
