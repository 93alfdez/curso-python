"""Ejercicio 1
Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio. Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta."""

price, discount = float(input("Dime un precio: ")), float(input("Dime el descuento: "))

def descuento(price, discount):
    return round(price*(1-(discount/100)), 2)

print(f"El precio con un descuento del {int(discount)}% es: {descuento(price, discount)} €")

def iva(price):
    return round(price*1.21, 2)

print(f"El precio con un descuento del 20% es: {iva(p)} €")

precios = {}

"""Ejercicio 2
Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al usuario
el valor y la función a aplicar, y mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros."""

"""Ejercicio 3
Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista."""

"""Ejercicio 4
Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana."""

"""Ejercicio 5
Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud."""

"""Ejercicio 6
Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.
"""

"""Ejercicio 7
Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
"""

"""Ejercicio 8
Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas aprobadas."""

"""Ejercicio 9
Escribir una función que calcule el módulo de un vector."""

"""Ejercicio 10
Escribir una función que reciba una muestra de números y devuelva los valores atípicos, es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3. Nota:
La puntuación típica de un valor se obtiene restando la media y dividiendo por la desviación típica de la muestra."""