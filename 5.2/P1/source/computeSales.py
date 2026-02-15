import sys
import pandas as pd

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
    if len(sys.argv) != 3:
        print("Usar: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)
    
    catalogo_precios = sys.argv[1]
    registro_ventas = sys.argv[2]
    print(f"Archivos: {catalogo_precios}, {registro_ventas}")

if __name__ == "__main__":
    main()