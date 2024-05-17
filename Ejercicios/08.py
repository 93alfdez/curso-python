# Crear una función que devuelva el imc pasandole como parametro la altura en cm y el peso en kg. Dicho programa debe mostrar en pantalla una advertencia si el imc es mayor de 24.9 diciendo que el "imc es alto" en caso contrario avisando que "imc normal"


def imc(h,p):
    return round((p/(h/100)**2),2)

h,p = float(input("Dime tu altura: ")), float(input("Dime tu peso: "))

if imc(h,p) > 24.9:
    print(f"El imc es alto")
else:
    print(f"El imc es normal")
