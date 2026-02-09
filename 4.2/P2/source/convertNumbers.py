# pylint: disable=invalid-name


"""
  Ejercicio 2. Convertir numeros
"""
import sys
import time

def convertir_binario(n):
    """Convertir numero entero a binario."""
    if n == 0:
        return "0"
    es_negativo = n < 0
    num = abs(int(n))
    num_binario = ""
    while num > 0:
        num_binario = str(num % 2) + num_binario
        num //= 2
    return "-" + num_binario if es_negativo else num_binario


def convertir_hexadecimal(n):
    """Convertir numero entero a hexadecimal."""
    if n == 0:
        return "0"
    hex_caracteres = "0123456789ABCDEF"
    es_negativo = n < 0
    num = abs(int(n))
    num_hexadecimal = ""
    while num > 0:
        num_hexadecimal = hex_caracteres[num % 16] + num_hexadecimal
        num //= 16
    return "-" + num_hexadecimal if es_negativo else num_hexadecimal


def process_file(ruta_archivo):
    """Leer el archivo y formatear los resultados."""
    resultado = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            for num_linea, linea in enumerate(file, 1):
                valor = linea.strip()
                if not valor:
                    continue
                try:
                    num = int(float(valor))
                    bin_val = convertir_binario(num)
                    hex_val = convertir_hexadecimal(num)
                    resultado.append((num, bin_val, hex_val))
                except ValueError:
                    print(f"Error: Dato invalido en la linea {num_linea}: '{valor}'")
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
        sys.exit(1)
    return resultado


def main():
    """Funcion principal"""
    inicia_timer = time.time()

    if len(sys.argv) != 2:
        print("Usar: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    archivo = sys.argv[1]
    datos_res = process_file(archivo)

    fin_timer = time.time()
    duracion_timer = fin_timer - inicia_timer

    resultado = []
    header = f"{'ITEM':<10} {'NUMERO':<15} {'BINARIO':<40} {'HEXADECIMAL':<15}"
    resultado.append(header)
    resultado.append("-" * 85)

    for i, (num, b, h) in enumerate(datos_res, 1):
        resultado.append(f"{i:<10} {num:<15} {b:<40} {h:<15}")

    resultado.append("-" * 85)
    resultado.append(f"Tiempo de ejecucion: {duracion_timer:.6f} segundos")

    resultado_final = "\n".join(resultado)

    print(resultado_final)
    with open("ConvertionResults.txt", "w", encoding='utf-8') as f:
        f.write(resultado_final)


if __name__ == "__main__":
    main()
