import sys
import json

def cargar_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no fue encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo {ruta_archivo} no tiene un formato JSON valido.")
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