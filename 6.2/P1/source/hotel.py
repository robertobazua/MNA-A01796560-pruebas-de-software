"""Modulo Hotel.py"""

import pandas as pd
from data_manager import cargar_dataframe, guardar_dataframe

ARCHIVO = "bd_hoteles.csv"
COLUMNAS = ["id", "nombre", "direccion", "cuartos_disponibles"]

class Hotel:
    """Clase Hotel"""

    @classmethod
    def crear_hotel(cls, id, nombre, direccion, cuartos_disponibles):
        """Crea un nuevo hotel en la BD"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        
        if id in df["id"].values:
            print(f"Error: Hotel {id} ya existe.")
            return False
        
        nuevo_reg = pd.DataFrame([[id, nombre, direccion, cuartos_disponibles]], columns=COLUMNAS)
        df = pd.concat([df, nuevo_reg], ignore_index=True)
        guardar_dataframe(df, ARCHIVO)
        return True
    
    @classmethod
    def eliminar_hotel(cls, id):
        """Elimina un hotel por ID"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        
        if id not in df["id"].values:
            print(f"Error: Hotel {id} no encontrado.")
            return False
        
        df = df[df["id"] != id]
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
    def modificar_hotel(cls, id, **kwargs):
        """Modifica los detalles de un hotel por ID"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        
        if id not in df["id"].values:
            print(f"Error: Hotel {id} no encontrado.")
            return False
        
        for key, value in kwargs.items():
            if key in COLUMNAS and key != "id":
                df.loc[df["id"] == id, key] = value
        
        guardar_dataframe(df, ARCHIVO)
        return True