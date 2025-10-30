# RETO FINAL PROGRAMACIÓN

# procesador_archivos.py
# Programa para trabajar archivos .txt y .csv
# Usar funciones, menú y matplotlib.

import os
import csv
import sys
import statistics
import matplotlib.pyplot as plt

# Funciones principales

def listar_archivos_en_ruta(ruta): # Lista los archivos en la ruta indicada
    try:
        archivos = os.listdir(ruta)  # Obtiene lista de archivos
    except Exception as e:
        print("Error al listar la ruta:", e)
        return []
    archivos_visibles = []
    for a in archivos:  # recorre cada archivo encontrado
        archivos_visibles.append(a)
    return archivos_visibles

def pedir_ruta_actual_o_otra(): # Pide al usuario confirmar la ruta
    print("Ruta actual:", os.getcwd())
    respuesta = input("¿Desea listar en la ruta actual? (indique s ó n): ").strip().lower()
    if respuesta == "s":
        ruta = os.getcwd()
    else:
        ruta = input("Ingrese la ruta para buscar archivos: ").strip()
        if not os.path.isdir(ruta):  # valida que la ruta exista
            print("La ruta no es válida. Usando ruta actual.")
            ruta = os.getcwd()
    return ruta


# Funciones para archivos .txt


def contar_palabras_caracteres(ruta_archivo): # Cuenta palabras y caracteres (con y sin espacios)
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
    except Exception as e:
        print("No se puede abrir el archivo:", e)
        return
    texto = archivo.read()
    archivo.close()

    palabras = [] # Cuenta palabras manualmente
    palabra_actual = ""
    for ch in texto:
        if ch.isspace():
            if palabra_actual != "":
                palabras.append(palabra_actual)
                palabra_actual = ""
        else:
            palabra_actual += ch
    if palabra_actual != "":
        palabras.append(palabra_actual)

    num_palabras = 0   # Contar elementos
    for p in palabras:
        num_palabras += 1

    num_caracteres_con_espacios = 0
    num_caracteres_sin_espacios = 0
    for ch in texto:
        num_caracteres_con_espacios += 1
        if not ch.isspace():
            num_caracteres_sin_espacios += 1

    # Mostrar resultados
    print("Resultado:")
    print("Número de palabras: ", num_palabras)
    print("Número de caracteres (con espacios): ", num_caracteres_con_espacios)
    print("Número de caracteres (sin espacios): ", num_caracteres_sin_espacios)

def reemplazar_palabra_en_archivo(ruta_archivo): # Reemplaza una palabra por otra en un archivo de texto
    palabra_buscar = input("Palabra a buscar (exacta): ").strip()
    if palabra_buscar == "":
        print("No ingresó ninguna palabra a buscar.")
        return
    palabra_reemplazo = input("Palabra de reemplazo: ").strip()

    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
    except Exception as e:
        print("No se pudo abrir el archivo:", e)
        return
    contenido = archivo.read()
    archivo.close()

    if palabra_buscar not in contenido:
        print("La palabra no se encontró en el archivo.")
        return

    contenido_nuevo = contenido.replace(palabra_buscar, palabra_reemplazo) # Reemplazar palabra en todo el texto

    try:                                        # Se crea un respaldo antes de sobrescribir para que no se pierda lo anterior
        backup_path = ruta_archivo + ".bak"
        archivo_bak = open(backup_path, "w", encoding="utf-8")
        archivo_bak.write(contenido)
        archivo_bak.close()
    except Exception as e:
        print("No se pudo crear respaldos:", e)
        return

    try:                                         # Reescribir el archivo modificado
        archivo_out = open(ruta_archivo, "w", encoding="utf-8")
        archivo_out.write(contenido_nuevo)
        archivo_out.close()
        print("Reemplazo completado. Se creó respaldo en", backup_path)
    except Exception as e:
        print("No se pudo escribir el archivo modificado:", e)

def histograma_vocales_txt(ruta_archivo):         # Se crea un histograma con el conteo de vocales
    try:
        archivo = open(ruta_archivo, "r", encoding="utf-8")
    except Exception as e:
        print("No se pudo abrir el archivo:", e)
        return
    texto = archivo.read().lower()
    archivo.close()

    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0} # Se cuentan las vocales que aparecen
    for ch in texto:
        if ch in vocales:
            vocales[ch] += 1

    print("Conteo de vocales:") # Se muestra el conteo de vocales
    for v in ['a','e','i','o','u']:
        print(v, ":", vocales[v])

    etiquetas = []             # Para graficar con matplotlib
    valores = []
    for v in ['a','e','i','o','u']:
        etiquetas.append(v)
        valores.append(vocales[v])

    plt.figure()
    plt.bar(etiquetas, valores)
    plt.title("Histograma de vocales")
    plt.xlabel("Vocal")
    plt.ylabel("Ocurrencias")
    plt.grid(axis='y', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()

# Funciones para archivos CSV

def mostrar_15_primeras_filas(ruta_archivo): # Muestra las primeras 15 filas de un archivo CSV
    try:
        archivo = open(ruta_archivo, newline='', encoding="utf-8")
    except Exception as e:
        print("No se pudo abrir el archivo:", e)
        return
    lector = csv.reader(archivo)
    fila_count = 0
    for fila in lector:
        print(fila)
        fila_count += 1
        if fila_count >= 15:
            break
    archivo.close()

def leer_csv_como_matriz(ruta_archivo):  # Carga un CSV completo en una lista de listas
    filas = []
    try:
        archivo = open(ruta_archivo, newline='', encoding="utf-8")
    except Exception as e:
        print("No se pudo abrir el archivo:", e)
        return filas
    lector = csv.reader(archivo)
    for fila in lector:
        filas.append(fila)
    archivo.close()
    return filas

def elegir_columna_por_nombre_o_indice(filas): # Permite al usuario elegir una columna por nombre
    if filas is None or len(filas) == 0:
        print("Archivo vacío o no leído.")
        return None, None
    encabezado = filas[0]
    print("Columnas encontradas:")
    i = 0
    for col in encabezado:
        print(str(i) + " - " + col)
        i += 1
    entrada = input("Ingrese el nombre de la columna exacto o su índice numérico: ").strip() # Si el usuario ingresa un número entonces se usa como índice
    try:
        idx = int(entrada)
        if idx < 0 or idx >= len(encabezado):
            print("Índice fuera de rango.")
            return None, None
        return idx, encabezado[idx]
    except:                           # Si no es número, se busca por nombre exacto
        j = 0
        encontrado = False
        for col in encabezado:
            if col == entrada:
                encontrado = True
                break
            j += 1
        if encontrado:
            return j, encabezado[j]
        else:
            print("No se encontró la columna por nombre, intente de nuevo.")
            return None, None

def convertir_columna_a_numeros(filas, indice_columna): # Convierte una columna en lista de números
    valores = []
    i = 1                                               # Para ignorar el encabezado
    while i < len(filas):
        fila = filas[i]
        if indice_columna < len(fila):
            celda = fila[indice_columna].strip()
            if celda != "":
                try:
                    numero = float(celda)
                    valores.append(numero)
                except:
                                                        # Para intentar con coma decimal por si el sistema que se está usando usa el punto
                    try:
                        celda_p = celda.replace(",", ".")
                        numero = float(celda_p)
                        valores.append(numero)
                    except:
                        pass  # ignorar no numérico
        i += 1
    return valores

def calcular_estadisticas_columna(filas, indice_columna):                  # Aquí se calculan las estadísticas de la columna
    valores = convertir_columna_a_numeros(filas, indice_columna)
    if len(valores) == 0:
        print("La columna no tiene datos numéricos o están vacíos.")
        return None
    resultado = {}
    # Cálculo de medidas estadísticas
    resultado['count'] = len(valores)
    try:
        resultado['mean'] = statistics.mean(valores)
    except:
        resultado['mean'] = None
    try:
        resultado['median'] = statistics.median(valores)
    except:
        resultado['median'] = None
    try:
        if len(valores) > 1:
            resultado['stdev'] = statistics.stdev(valores)
        else:
            resultado['stdev'] = 0.0
    except:
        resultado['stdev'] = None
    try:
        resultado['max'] = max(valores)
        resultado['min'] = min(valores)
    except:
        resultado['max'] = None
        resultado['min'] = None
    resultado['valores'] = valores
    return resultado

def graficar_columna_scatter_y_barras(filas, indice_columna):        # Grafica una columna con dispersión y barras
    valores = convertir_columna_a_numeros(filas, indice_columna)
    if len(valores) == 0:
        print("No hay datos numéricos para graficar.")
        return

    # Para el gráfico de dispersión
    plt.figure()
    x = []
    i = 0
    while i < len(valores):
        x.append(i)
        i += 1
    plt.scatter(x, valores)
    plt.title("Gráfico de dispersión - columna índice " + str(indice_columna))
    plt.xlabel("Índice de fila (orden)")
    plt.ylabel("Valor")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Se ordenan los datos para gráfico de barras
    valores_ordenados = list(valores)
    n = len(valores_ordenados)
    j = 0
    while j < n:
        k = 0
        while k < n - 1:
            if valores_ordenados[k] > valores_ordenados[k+1]:
                tmp = valores_ordenados[k]
                valores_ordenados[k] = valores_ordenados[k+1]
                valores_ordenados[k+1] = tmp
            k += 1
        j += 1

    # Se toman los primeros 10 valores para el gráfico
    top_n = 10
    if len(valores_ordenados) < top_n:
        top_n = len(valores_ordenados)

    etiquetas = []
    barras = []
    p = 0
    while p < top_n:
        etiquetas.append(str(p+1))
        barras.append(valores_ordenados[p])
        p += 1

    plt.figure()
    plt.bar(etiquetas, barras)
    plt.title("Valores ordenados - primeros " + str(top_n))
    plt.xlabel("Elemento ordenado (1..N)")
    plt.ylabel("Valor")
    plt.tight_layout()
    plt.show()

# Menú de navegacióon

# Primer menú para los txt
def submenu_txt():
    ruta = input("Ingrese la ruta completa del archivo .txt: ").strip()
    if not os.path.isfile(ruta):
        print("Archivo no encontrado.")
        return
    while True:
        print("\nSubmenú para .txt")
        print("1 - Contar número de palabras y caracteres")
        print("2 - Reemplazar una palabra por otra (crea respaldo .bak)")
        print("3 - Histograma de ocurrencia de las vocales")
        print("4 - Volver")
        opcion = input("Elija una opción: ").strip()
        if opcion == "1":
            contar_palabras_caracteres(ruta)
        elif opcion == "2":
            reemplazar_palabra_en_archivo(ruta)
        elif opcion == "3":
            histograma_vocales_txt(ruta)
        elif opcion == "4":
            break
        else:
            print("Opción inválida, intente de nuevo.")

# Segundo menú para los archivos CSV
def submenu_csv():
    ruta = input("Ingrese la ruta completa del archivo .csv: ").strip()
    if not os.path.isfile(ruta):
        print("Archivo no encontrado.")
        return
    filas = leer_csv_como_matriz(ruta)
    if filas is None or len(filas) == 0:
        print("No fue posible leer el CSV o está vacío.")
        return
    while True:
        print("\nSubmenú para .csv")
        print("1 - Mostrar las 15 primeras filas")
        print("2 - Calcular estadísticas de una columna")
        print("3 - Graficar una columna completa (dispersión + barras)")
        print("4 - Volver")
        opcion = input("Elija una opción: ").strip()
        if opcion == "1":
            mostrar_15_primeras_filas(ruta)
        elif opcion == "2":
            idx, nombre = elegir_columna_por_nombre_o_indice(filas)
            if idx is not None:
                stats = calcular_estadisticas_columna(filas, idx)
                if stats is not None:
                    # Mostrar resultados en consola
                    print("Estadísticas para columna:", nombre)
                    print("Número de datos:", stats['count'])
                    print("Promedio:", stats['mean'])
                    print("Mediana:", stats['median'])
                    print("Desviación estándar:", stats['stdev'])
                    print("Máximo:", stats['max'])
                    print("Mínimo:", stats['min'])
        elif opcion == "3":
            idx, nombre = elegir_columna_por_nombre_o_indice(filas)
            if idx is not None:
                graficar_columna_scatter_y_barras(filas, idx)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

# Función principal
def main():
    print("Procesador de archivos .txt y .csv")
    while True:
        print("\nMenú Principal")
        print("1 - Listar archivos en la ruta (o ingresar otra ruta)")
        print("2 - Procesar archivo de texto (.txt)")
        print("3 - Procesar archivo separado por comas (.csv)")
        print("4 - Salir")
        opcion = input("Elige opción: ").strip()
        if opcion == "1":
            ruta = pedir_ruta_actual_o_otra()
            archivos = listar_archivos_en_ruta(ruta)
            if len(archivos) == 0:
                print("No encontré archivos en la ruta.")
            else:
                print("Archivos en", ruta)
                for a in archivos:
                    print(" -", a)
        elif opcion == "2":
            submenu_txt()
        elif opcion == "3":
            submenu_csv()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

# Inicio del programa como tal
if __name__ == "__main__":
    main()