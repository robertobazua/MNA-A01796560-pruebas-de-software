import sys

def main():
    if len(sys.argv) != 3:
        print("Usar: python computeSales.py priceCatalogue.json salesRecord.json")
        sys.exit(1)
    
    catalogo_precios = sys.argv[1]
    registro_ventas = sys.argv[2]
    print(f"Archivos: {catalogo_precios}, {registro_ventas}")

if __name__ == "__main__":
    main()