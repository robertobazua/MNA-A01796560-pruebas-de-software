# pylint: disable=R0801
"""Modulo Reservacion.py"""

import pandas as pd
from source.cliente import Cliente
from source.hotel import Hotel
from source.data_manager import cargar_dataframe, guardar_dataframe

ARCHIVO = "bd_reservaciones.csv"
COLUMNAS = ["id_reservacion", "id_cliente", "id_hotel", "disponibilidad"]


class Reservacion:
    """Clase Reservacion"""

    @classmethod
    def crear_reservacion(cls, id_reservacion, id_cliente,
                          id_hotel, disponibilidad):
        """Crea una nueva reservacion en la BD"""

        df_cli = Cliente.listar_clientes()

        if df_cli.empty or id_cliente not in df_cli["id_cliente"].values:
            print(f"Error: Cliente {id_cliente} no encontrado.")
            return False

        df_hoteles = Hotel.listar_hoteles()

        if df_hoteles.empty or id_hotel not in df_hoteles["id_hotel"].values:
            print(f"Error: Hotel {id_hotel} no encontrado.")
            return False

        df = cargar_dataframe(ARCHIVO, COLUMNAS)

        if id_reservacion in df["id_reservacion"].values:
            print(f"Error: Reservacion {id_reservacion} ya existe.")
            return False
        nuevo_reg = pd.DataFrame([[id_reservacion, id_cliente, id_hotel,
                                   disponibilidad]], columns=COLUMNAS)
        df = pd.concat([df, nuevo_reg], ignore_index=True)
        guardar_dataframe(df, ARCHIVO)
        return True

    @classmethod
    def cancelar_reservacion(cls, id_reservacion):
        """Elimina una reservacion por ID"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)

        if id_reservacion not in df["id_reservacion"].values:
            print(f"Error: Reservacion {id_reservacion} no encontrada.")
            return False

        df = df[df["id_reservacion"] != id_reservacion]
        guardar_dataframe(df, ARCHIVO)
        return True

    @classmethod
    def listar_reservaciones(cls):
        """Lista todas las reservaciones"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)

        if df.empty:
            print("No hay reservaciones registradas.")
            return df

        print(df.to_string(index=False))
        return df
