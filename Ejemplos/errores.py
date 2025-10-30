try:
    entero = int(input("Ingrese un número: "))
except ValueError:
    print("El valor ingresado no es un número.")
else:
    print("La operación se realizó correctamente.")
finally:
    print("Puedes continuar con el programa.")


print(entero)