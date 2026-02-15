# pylint: disable=invalid-name
"""
Programa: computeSales.py
Actividad 5. Calcula el costo total de las ventas.
"""

import sys
import time
import pandas as pd


def cargar_archivo(ruta_archivo):
    """Funcion para cargar los archivos JSON en DataFrames de Pandas."""
    try:
        archivo = pd.read_json(ruta_archivo)
        return archivo
    except FileNotFoundError as error:
        print(f"Error: El arhivo no existe en la ruta. {error}")
        return None
    except ValueError as error:
        print(f"Error: El archivo no tiene formato JSON valido. {error}")
        return None
    except PermissionError as error:
        print(f"Error: No se tienen permisos para el archivo. {error}")
        return None
    return None


def validar_calogo_precios(df_precios):
    """Funcion para validar columnas necesarias del catalogo de precios."""
    if 'title' not in df_precios or 'price' not in df_precios:
        print("Error: El catalogo no tiene las columnas 'title' o 'price'")
        return False
    return True


def calcular_totales(df_precios, df_ventas):
    """Funcion para calcular el total de la venta."""

    df_merge = pd.merge(
        df_ventas,
        df_precios[['title', 'price']],
        left_on='Product',
        right_on='title',
        how='left'
    )

    print(df_merge)

    ventas_invalidas = df_merge[df_merge['price'].isna()]

    print(ventas_invalidas)

    if not ventas_invalidas.empty:
        for producto in ventas_invalidas['Product'].unique():
            print(f"Error: El producto '{producto}' no existe en el catalogo.")

    df_merge['subtotal'] = df_merge['price'] * df_merge['Quantity']

    return df_merge['subtotal'].sum()


def main():
    """Funcion principal para la ejecucion de computeSales."""

    inicia_tiempo = time.time()

    if len(sys.argv) != 3:
        print("Error: Numero de parametros incorrecto")
        sys.exit(1)
    ruta = ""
    catalogo_precios = ruta + sys.argv[1]
    registro_ventas = ruta + sys.argv[2]
    print(f"Archivos: {catalogo_precios}, {registro_ventas}")

    df_precios = cargar_archivo(catalogo_precios)
    df_ventas = cargar_archivo(registro_ventas)

    if validar_calogo_precios(df_precios) is False:
        sys.exit(1)

    total = calcular_totales(df_precios, df_ventas)

    print(f"Total: {total}")

    tiempo_ejecucion = time.time() - inicia_tiempo

    print(f"Tiempo de ejecucion: {tiempo_ejecucion:.4f} segundos")


if __name__ == "__main__":
    main()
