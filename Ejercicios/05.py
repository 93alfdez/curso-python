"""1. Hacer un programa que escriba la frase "Hola Mundo" por pantalla."""
# print(f"hola mundo")

"""2. Hacer un programa que escriba la frase "Hola Mundo" por pantalla."""
# m = "hola mundo"
# print(m)

"""3. Escribir un programa que pregunte el nombre del usuario en la consola y después de
que el usuario lo introduzca muestre por pantalla la cadena ¡ Hola <nombre> !, donde
<nombre> es el nombre que el usuario haya introducido."""

# n = input("¿Cuál es tu nombre? ")
# print(f"Hola {n}")

"""4. Escribir un programa que muestre por pantalla el resultado de la siguiente operación
aritmética (3+5/2*5)2."""

# n1 = 3+2
# n2 = 2*5
# print((n1/n2)**2)

"""5. Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
coste por hora. Después debe mostrar por pantalla la paga que le corresponde."""

# h , c = int(input("¿Cuantas horas has trabajado? ")) , int(input("¿Cuanto te pagan por hora? "))
# t = (h*c)
# print(f"Tienen que pagarte {t}")

"""6. Escribir un programa que lea un entero positivo, n, introducido por el usuario y después
muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros
enteros positivos puede ser calculada de la siguiente forma:"""

# n = int(float(input("Dame un número: ")))
# s = n*(n+1)/2
# print(f'La suma es {s}')


"""7. Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule
el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase
Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal
calculado redondeado con dos decimales."""
# p , e = float(input("¿Cual es tu peso? ")) , float(input("¿Cuanto mides? "))
# imc = (p/e)
# print(f'Tu índice de masa corporal es {"%.2f" % imc}')


"""8. Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la división
<n> entre <m> da un cociente <c> y un resto < r> donde <n> y <m> son los números
introducidos por el usuario, y <c> y < r> son el cociente y el resto de la división
entera respectivamente."""
# n1 , n2 = int(input("Dame el primer número: ")) , int(input("Dame el segundo número: "))
# c = n1//n2
# r = n1%n2

# print(f'La división de {n1} entre {n2} da un cociente {c} y un resto {r}')

"""9. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y
el número de años, y muestre por pantalla el capital obtenido en la inversión."""

# c , i, a = int(float(input("¿Qué cantidad quieres invertir? "))), int(float(input("¿A que interés? "))), int(input("¿Cuantos años? "))
# t = (c*i)*a

# print(f"El capital obtenido es de {t} €")