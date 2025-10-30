ruta = "C:\\Users\\B09S202est\\Downloads"
#\ secuencia de escape: \n \t \ --> \\
file_name = "aviaciones.txt"
modo = "a"
fp = open(ruta+"\\"+file_name, modo, encoding="utf-8")
nombre = input("Ingrese el nombre de un avión: ")
peso = int(input("Ingrese el peso del avión: "))
velocidad = float(input("Velocidad máxima: "))
fp.write(nombre + "\n")
fp.write(str(peso))
fp.write("\n")
fp.write(str(velocidad))
fp.close()