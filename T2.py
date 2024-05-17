# Funciones

# def <<nombre funcion>>(<<variables>>):
    # <<cuerpo>>
    # return <<devolucion>>

# nombre = input("Tu nombre: ")

# def saludar(nombre):
#     return "hola " + nombre

# print(f"Te dicen: {saludar(nombre)}")

# Crear un programa que pida al usuario un número entero positivo y que invoque a una función llamada cuadrado que devuelva el cuadrado del número que se le pase por parámetro


def cuadrado(n):
    return n**2

n = int(float(input("Dame un número ")))

print(f"El cuadrado del {n} es {cuadrado(n)}")