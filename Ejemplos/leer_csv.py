import csv
temperatura = []
humedad = []
presion = []
velocidad = []
with open('C:\\Users\\B09S202est\\Desktop\\Variables.csv', 'r') as csvfile: # Usamos el manejador de contexto
    lector = csv.reader(csvfile, delimiter=';') # Se utiliza el método reader
    encabezado = next(lector)
    for fila in lector:                         # Con el for se itera sobre el objeto para leer
        dato = fila[0]
        dato = float(dato.replace(',','.'))
        temperatura.append(dato)
    for fila in lector:                         # Con el for se itera sobre el objeto para leer
        dato = fila[1]
        dato = float(dato.replace(',','.'))
        humedad.append(dato) 
    for fila in lector:                         # Con el for se itera sobre el objeto para leer
        dato = fila[2]
        dato = float(dato.replace(',','.'))
        presion.append(dato)
    for fila in lector:
        dato = fila[3]
        dato = float(dato.replace('.',','))
        velocidad.append(dato)

print(encabezado[0])
print(temperatura)
print(encabezado[1])
print(humedad)
print(encabezado[2])
print(presion)
print(encabezado[3])
print(velocidad)