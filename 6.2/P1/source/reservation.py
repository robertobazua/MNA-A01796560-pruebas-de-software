"""Modulo Reservation.py"""

import pandas as pd
from data_manager import cargar_dataframe, guardar_dataframe

ARCHIVO = "bd_reservaciones.csv"
COLUMNAS = ["id", "cliente_id", "hotel_id"]

class Reservation:
    """Clase Reservation"""

    @classmethod
    def crear_reservacion(cls, id, cliente_id, hotel_id):
        """Crea una nueva reservacion en la BD"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        
        if id in df["id"].values:
            print(f"Error: Reservacion {id} ya existe.")
            return False
        
        nuevo_reg = pd.DataFrame([[id, cliente_id, hotel_id]], columns=COLUMNAS)
        df = pd.concat([df, nuevo_reg], ignore_index=True)
        guardar_dataframe(df, ARCHIVO)
        return True
    
    @classmethod
    def eliminar_reservacion(cls, id):
        """Elimina una reservacion por ID"""

        df = cargar_dataframe(ARCHIVO, COLUMNAS)
        
        if id not in df["id"].values:
            print(f"Error: Reservacion {id} no encontrada.")
            return False
        
        df = df[df["id"] != id]
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