# Crear una función llamada media que realice la media aritmética de dos valores pasados a la función

def media(x,y):
    return (x+y)/2

x, y = int(input("Primer valor: ")), int(input("Segundo valor: "))

print(f"La media es: {media(x,y)}")