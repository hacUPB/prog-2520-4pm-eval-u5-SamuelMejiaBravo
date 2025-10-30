
lista = ["uno", "dos", "tres", "cuatro", "cinco"]
ruta = "C:\\Users\\B09S202est\\Downloads"
#\ secuencia de escape: \n \t \ --> \\
file_name = "canciones.txt"
file_info = ruta+"\\"+file_name
modo = "r"
with open(file_info, modo, encoding="utf-8") as archivo:
    # Hacer operaciones con el archivo
    for dato in archivo:
        print(dato)