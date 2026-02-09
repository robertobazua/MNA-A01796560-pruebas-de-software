# pylint: disable=invalid-name

"""
Ejercicio 1. Calcular Estadisticas 
"""
import sys
import time

def leer_archivo(ruta_archivo):
    """
    Req1. Leer el archivo de la lista de elementos que se recibio por parametro.
    Req3. Manejar datos invalidos del archivo mostrandolos por consola y continuando la ejecucion.
    """
    datos = []
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as file:
            for num_linea, linea in enumerate(file, 1):
                dato = linea.strip()
                if not dato:
                    continue
                try:
                    number = float(dato)
                    datos.append(number)
                except ValueError:
                    print(f"Error: Dato invalido en la linea {num_linea}: '{dato}'")
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
        sys.exit(1)

    return datos


def calcular_media(datos):
    """Calcular la media."""
    if not datos:
        return 0.0
    return sum(datos) / len(datos)


def calcular_mediana(datos):
    """Calcular la mediana."""
    if not datos:
        return 0.0
    datos_ordenados = sorted(datos)
    cont = len(datos_ordenados)
    pos = cont // 2

    if cont % 2 == 0:
        return (datos_ordenados[pos - 1] + datos_ordenados[pos]) / 2
    return datos_ordenados[pos]


def calcular_moda(datos):
    """Calcular la moda. Regrasar una lista en caso de haber una moda multiple."""
    if not datos:
        return []
    frecuencias = {}
    for item in datos:
        if item in frecuencias:
            frecuencias[item] += 1
        else:
            frecuencias[item] = 1

    max_frec = max(frecuencias.values())
    modas = [k for k, v in frecuencias.items() if v == max_frec]
    return modas


def calcular_varianza(datos, media):
    """Calcular la varianza."""
    if len(datos) < 2:
        return 0.0
    return sum((x - media) ** 2 for x in datos) / (len(datos) - 1)


def calcular_desviacion(varianza):
    """Calcular la desviacion estandar."""
    return varianza ** 0.5


def main():
    """Funcion principal"""
    inicia_timer = time.time()

    if len(sys.argv) != 2:
        print("Usar: python computeStatistics.py fileWithData.txt")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    data_points = leer_archivo(ruta_archivo)

    if not data_points:
        print("No se encontraron datos validos en el archivo.")
        sys.exit(1)

    # Calculos
    mean_val = calcular_media(data_points)
    median_val = calcular_mediana(data_points)
    mode_val = calcular_moda(data_points)
    variance_val = calcular_varianza(data_points, mean_val)
    std_dev_val = calcular_desviacion(variance_val)

    fin_timer = time.time()
    elapsed_time = fin_timer - inicia_timer

    # Formatear resultados
    resultado = []
    resultado.append("Resultado de las estadisticas")
    resultado.append("-" * 30)
    resultado.append(f"Media: {mean_val:.5f}")
    resultado.append(f"Mediana: {median_val:.5f}")
    resultado.append(f"Moda: {mode_val}")
    resultado.append(f"Desviacion Estandar: {std_dev_val:.5f}")
    resultado.append(f"Varianza: {variance_val:.5f}")
    resultado.append(f"Tiempo de ejecucion: {elapsed_time:.6f} segundos")

    resultado_final = "\n".join(resultado)

    # Req2. Imprimir todos los resultados en una pantalla
    print(resultado_final)

    # Req2. Los resultados generados se almancenan en un archivo llamado StatisticsResults.txt
    with open("StatisticsResults.txt", "w", encoding='utf-8') as out_file:
        out_file.write(resultado_final)


if __name__ == "__main__":
    main()
