# Ejercicio 1
# p = input("Dame una palabra: ")
# # while a < 10 :
# #     print(p)
# #     a+=1

# Ejercicio 2
# edad = int(input("dime tu edad: "))
# y = 1
# # while y <= edad :
# #     print(y)
# #     y+=1

# for y in range(edad) :
#         print(y+1)

# Ejercicio 3
# n = int(input("dime un número: "))

# for i in range(1,n):
#     if i%2 != 0:
#         print(i)

# i = 1
# while i <= n:
#     print((2*i)+1)
#     i+=1


# Ejercicio 4
# n = int(input("dime un número: "))
# for i in range(n, 0, -1):
#     print(i, end=",")


# Ejercicio 5
# ci , n, i = float(input("¿Qué cantidad quieres invertir? ")), int(input("¿Cuantos años? ")), int(input("Interés %: "))
# i = 0.04

# for k in range(1,n+1):
#     ci = ci*(1+i)**k
#     print(f"El año nº: {k} obtendrás un capital de {ci:.2f} €")


# # Ejercicio 6
# n = int(input("dime un número: "))
# for i in range(1,n+1):
#     print("*"*i)

# Ejercicio 7

# for i in range(11):
#     for a in range(11):
#         print(f"{i} x {a} = {a*i}")

# Ejercicio 8


# n = int(input("dime un número: "))
# for i in range(1,n+1,2):
#     for a in range(i, 0, -2):
#             print(a,end=" ")
#     print("")


# Ejercicio 9
    # c = input("contraseña: ")
    # C=""
    # while c != C:
    #     print("Contraseña incorrecta")
    #     C = input("introduce contraseña")

# Ejercicio 10
# n, i = int(input("dime un número: ")), 2

# while n% i != 0:
#     i+=1
#     if n == i:
#         print("es primo")
#     else:
#          print("no es primo")

# Ejercicio 11
# p = input("palabra: ")

# for k in range(len(p)-1, -1, -1):
#     print(p[k])

# x = len(p)
# while len(p) <= x :
#     x-=1
#     print(p[k])


# Ejercicio 12
# f, l, c = input("frase: "), input("letra: "), 0

# for k in f:
#     if k == l:
#         c+=1

# print(f"la letra {l} aparece {c} veces en la frase {f}")

# Ejercicio 13

x = True

while x:
    v = input(":")
    if v == "salir":
        x = False
    else:
        print(v)