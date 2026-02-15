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

    tiempo_ejecucion = time.time() - inicia_tiempo

    print(f"Tiempo de ejecucion: {tiempo_ejecucion:.4f} segundos")

if __name__ == "__main__":
    main()