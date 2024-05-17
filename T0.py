## Asignación: <<variable>> = <valor>

# TIPOS DE DATOS

## numericos -> todos los números (0-9)

### suma: + // resta: - // multiplicacion: * // division decimal: /
### division entera (cociente): // | resto: %
### mayor > // menor < // mayor o igual >= // menor o igual <= // igual: ==
### exponenciacion: ** // trigonométricas: <<importar math>>
## string -> "<<texto>>" '<<texto>>'
## booleanos -> True // False
## y: and // o: or // distinto: != // ni: not(<<>>)
### concatenar: + // replicacion: * // comparacion: == // posicional : < >

### True and True = True // False and True = True and False = False // False and False = False
### True or True = True // True or False = False  True or True // False or False = False


a = 4
b = 3

print(a/b)


c = int(c) #convierte a número entero
c = float(c) #convierte string a string



# CADENAS DE TEXTO
## len(<string>) -> longitud del str
## indice: posicion que ocupa un caracter dentro del str
## <var str>[<indice>]
##.upper() -> convierte a mayus
## .lower() -> convierte a minus
## .replace(<caracter a buscar>,<caracter a cambiar>)
## .strip() -> eliminar espacios
## .title() -> convierte la primera letra de cada palabra en mayus
## .capitalize() -> capitalizar el str
## .find(<caracter a buscar>) -> devuelve el indice de la primera coincidencia

a = "Hola "
print(a[3])