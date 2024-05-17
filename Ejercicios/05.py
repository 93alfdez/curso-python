"""1. Hacer un programa que escriba la frase "Hola Mundo" por pantalla."""
# print(f"hola mundo")

"""2. Escribir un programa que almacene la cadena ¡ Hola Mundo ! en una variable y luego
muestre por pantalla el contenido de la variable."""
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

# h , c = int(float(input("¿Cuantas horas has trabajado? "))) , int(float(input("¿Cuanto te pagan por hora? ")))
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
# imc = round(p/(e**2),2)
# print(f'Tu índice de masa corporal es imc')


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

# c , i, a = float(input("¿Qué cantidad quieres invertir? ")), float(input("¿A que interés? ")), int(input("¿Cuantos años? "))
# t = round((c*(1+(i/100)))**a, 2)

# print(f"El capital obtenido es de {t} €")



"""10. Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado."""

# numP = int(float(input("¿Cuantos payasos quieres comprar? ")));
# numM = int(float(input("¿Cuantas muñecas quieres comprar? ")));

# pesoP = 112
# pesoM = 75

# print(f"Se han vendido {numP} payasos y {numM} muñecas. El peso total del paquete es {(numP*pesoP)+(numM*pesoM)} g")

"""11. Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales."""

# ah = float(input("¿Qué cantidad de ahorros tienes? "));
# i = 0.04

# n1,n2,n3,n4 = 1,2,3,4

# y1 = ah*((1+i)**n1), 2
# y2 = y1*((1+i)**n2),2
# y3 = y2*((1+i)**n3),2
# y4 = y3*((1+i)**n4),2

# print(f"Después del primer año la cantidad de ahorros es: {y1:.2f} €\nSegundo año sería: {y2:.2f} €\nTercer año: {y3:.2f} €\nCuarto año: {y4:.2f} €")

"""12. Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Despunés el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total."""

p = int(input("¿Cuantas barras se han vendido que no son frescas? "));
P = p*3.49
d = p*3.49*0.60
T = p*3.49*0.40

print(f"\nBarra de pan: 3,49€   {p} ud   {"%.2f" % P}€\nDescuento -60%: -{"%.2f" % d}€\nTotal con descuento: {"%.2f" % T}€")