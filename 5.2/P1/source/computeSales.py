import sys
import pandas as pd
import time

def cargar_archivo(ruta_archivo):
    try:
        archivo = pd.read_json(ruta_archivo)
        return archivo
    except ValueError as error:
        print(f"Error: El archivo no tiene formato JSON valido. {error}")
        return None
    except Exception as error:
        print(f"Error: Se produjo un error inesperado al cargar el archivo. {error}")
        return None

def validar_calogo_precios(df_precios):
    try:
        if 'title' not in df_precios or 'price' not in df_precios:
            print("Error: El catalogo no tiene las columnas 'title' o 'price'")
            return None
    except Exception as error:
        print(f"Error: Ocurrio un error al validar el catalogo de precios")
        return None
    
    return 1

def calcular_totales(df_precios, df_ventas):

    df_merge = pd.merge(
        df_ventas,
        df_precios[['title', 'price']],
        left_on = 'Product',
        right_on = 'title',
        how = 'left'
    )

    ventas_invalidas = df_merge[df_merge['price'].isna()]

    if not ventas_invalidas.empty:
        for producto in ventas_invalidas['Product'].unique():
            print(f"Error: El producto '{producto}' no existe en el catalogo.")

    df_merge['subtotal'] = df_merge['price'] * df_merge['Quantity']

    return df_merge['subtotal'].sum()

def main():

    inicia_tiempo = time.time()

    if len(sys.argv) != 3:
        print("Usar: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)
    
    ruta = ""
    catalogo_precios = ruta + sys.argv[1]
    registro_ventas = ruta + sys.argv[2]
    print(f"Archivos: {catalogo_precios}, {registro_ventas}")

    df_precios = cargar_archivo(catalogo_precios)
    df_ventas = cargar_archivo(registro_ventas)

    if validar_calogo_precios(df_precios) is None:
        sys.exit(1)

    total = calcular_totales(df_precios, df_ventas)

    print(f"Total: {total}")

    tiempo_ejecucion = time.time() - inicia_tiempo

    print(f"Tiempo de ejecucion: {tiempo_ejecucion:.4f} segundos")

if __name__ == "__main__":
    main()