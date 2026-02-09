# pylint: disable=invalid-name
"""
Ejercicio 3. Contar palabras
"""

import sys
import time


def contador_palabras(ruta_archivo):
    """
    Contar la frecuencia de las palabras
    """
    cont = {}
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            for linea_num, linea in enumerate(file, 1):
                try:
                    palabras = linea.strip().split()
                    if not palabras:
                        continue
                    for palabra in palabras:
                        palabra = palabra.lower()
                        if palabra in cont:
                            cont[palabra] += 1
                        else:
                            cont[palabra] = 1
                except (ValueError, UnicodeDecodeError) as error:
                    print(f"Error: Dato invalido en la linea {linea_num}: {error}")
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
        sys.exit(1)
    return cont


def main():
    """Funcion principal"""
    inicia_timer = time.time()

    if len(sys.argv) != 2:
        print("Usar: python wordCount.py fileWithData.txt")
        sys.exit(1)

    archivo = sys.argv[1]
    frequencies = contador_palabras(archivo)

    fin_timer = time.time()
    duracion = fin_timer - inicia_timer

    # Formatear resultados
    salida = []
    salida.append(f"{'PALABRA':<15} {'FRECUENCIA':<10}")
    salida.append("-" * 25)
    # Ordenar de mayor a menor frencuencia
    for word, count in sorted(frequencies.items(), key=lambda item: item[1], reverse=True):
        salida.append(f"{word:<15} {count:<10}")

    salida.append("-" * 25)
    salida.append(f"Tiempo de ejecucion: {duracion:.6f} segundos")

    resultado = "\n".join(salida)

    print(resultado)
    with open("WordCountResults.txt", "w", encoding='utf-8') as f:
        f.write(resultado)

if __name__ == "__main__":
    main()
