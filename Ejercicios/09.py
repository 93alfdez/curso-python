# Crear una función que verifique que la contraseña metida por el usuario comienza por mayus y es una vocal en caso de no ser correcta pedir al usuario que vuelva a intentar introducir la contraseña

def verificar(pw):
    if pw[0] == "A" or pw[0] == "E" or pw[0] == "I" or pw[0] == "O" or pw[0] == "U":
        pass # si se cumple va al return
    else:
        pw = input("Contraseña incorrecta, introduce de nuevo: ")
    return pw

pw = input("contraseña que comience por mayuscula y vocal: ")





