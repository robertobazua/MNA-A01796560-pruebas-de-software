"""Modulo Reservacion.py"""

import pandas as pd
from source.data_manager import cargar_dataframe, guardar_dataframe

ARCHIVO = "bd_reservaciones.csv"
COLUMNAS = ["id_reservacion", "id_cliente", "id_hotel"]


class Reservacion:
    """Clase Reservacion"""

    @classmethod
    def crear_reservacion(cls, id_reservacion, id_cliente, id_hotel):
        """Crea una nueva reservacion en la BD"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)

        if id in df["id_reservacion"].values:
            print(f"Error: Reservacion {id_reservacion} ya existe.")
            return False
        nuevo_reg = pd.DataFrame([[id_reservacion, id_cliente, id_hotel]],
                                 columns=COLUMNAS)
        df = pd.concat([df, nuevo_reg], ignore_index=True)
        guardar_dataframe(df, ARCHIVO)
        return True

    @classmethod
    def eliminar_reservacion(cls, id_reservacion):
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
            return False

        print(df.to_string(index=False))
        return df
