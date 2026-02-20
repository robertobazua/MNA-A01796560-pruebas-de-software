"""Modulo Cliente.py"""

import pandas as pd
from data_manager import cargar_dataframe, guardar_dataframe

ARCHIVO = "bd_clientes.csv"
COLUMNAS = ["id_cliente", "nombre", "email"]


class Cliente:
    """Clase Cliente"""

    @classmethod
    def crear_cliente(cls, id_cliente, nombre, email):
        """Crear cliente en la BD"""
        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        if id_cliente in df["id_cliente"].values:
            print(f"Error: Cliente {id_cliente} ya existe.")
            return False
        nuevo_reg = pd.DataFrame([[id_cliente, nombre, email]], columns=COLUMNAS)
        df = pd.concat([df, nuevo_reg], ignore_index=True)
        guardar_dataframe(df, ARCHIVO)
        return True

    @classmethod
    def eliminar_cliente(cls, id_cliente):
        """Elimina un cliente por ID"""
        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        if id_cliente not in df["id"].values:
            print(f"Error: Cliente {id_cliente} no encontrado.")
            return False
        df = df[df["id_cliente"] != id_cliente]
        guardar_dataframe(df, ARCHIVO)
        return True

    @classmethod
    def listar_clientes(cls, id_cliente):
        """Lista todos los clientes"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        row = df[df["id_cliente"] == id_cliente]

        if row.empty:
            print(f"Error: Cliente {id_cliente} no encontrado.")
            return False
        print(row.to_string(index=False))
        return row
