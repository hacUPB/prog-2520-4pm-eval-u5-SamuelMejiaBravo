#1. Abrir el archivo
fp = open("C:\\Users\\B09S202est\\Desktop\\leer.txt", "r", encoding="utf-8")
#2. Leer el archivo
# datos = fp.read(20) # El paréntesis es la cantidad de caracteres
# datos = fp.read()
fp.readline()
fp.read(5)
datos = fp.readline()
#3. Cerrar el archivo
fp.close()

print(datos)