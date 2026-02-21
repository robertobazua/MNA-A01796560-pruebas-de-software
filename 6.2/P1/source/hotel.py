"""Modulo Hotel.py"""

import pandas as pd
from source.data_manager import cargar_dataframe, guardar_dataframe

ARCHIVO = "bd_hoteles.csv"
COLUMNAS = ["id_hotel", "nombre", "direccion", "disponibilidad"]


class Hotel:
    """Clase Hotel"""

    @classmethod
    def crear_hotel(cls, id_hotel, nombre, direccion, disponibilidad):
        """Crea un nuevo hotel en la BD"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        if id_hotel in df["id_hotel"].values:
            print(f"Error: Hotel {id_hotel} ya existe.")
            return False
        nuevo_reg = pd.DataFrame([[id_hotel, nombre, direccion,
                                   disponibilidad]], columns=COLUMNAS)
        df = pd.concat([df, nuevo_reg], ignore_index=True)
        guardar_dataframe(df, ARCHIVO)
        return True

    @classmethod
    def eliminar_hotel(cls, id_hotel):
        """Elimina un hotel por ID"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        if id_hotel not in df["id_hotel"].values:
            print(f"Error: Hotel {id_hotel} no encontrado.")
            return False
        df = df[df["id_hotel"] != id_hotel]
        guardar_dataframe(df, ARCHIVO)
        return True

    @classmethod
    def listar_hoteles(cls):
        """Lista todos los hoteles"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        if df.empty:
            print("No hay hoteles registrados.")
            return False
        print(df.to_string(index=False))
        return df

    @classmethod
    def modificar_hotel(cls, id_hotel, **kwargs):
        """Modifica los detalles de un hotel por ID"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        if id_hotel not in df["id_hotel"].values:
            print(f"Error: Hotel {id_hotel} no encontrado.")
            return False

        for key, value in kwargs.items():

            if key in COLUMNAS and key != "id_hotel":
                df.loc[df["id_hotel"] == id_hotel, key] = value
        guardar_dataframe(df, ARCHIVO)
        return True
