""" Sea un str "juan jose es un mal jefe, solo sabe exigir y no recompensar", se pide:
    a) Eliminar espacios inicio y final
    b) Convertir a mayusculas la primera letra
    c) Averiguar cuantos caracteres tiene, y encontrar la primera posicion de la letra "a"
    d) Contar cuantas veces aparece la letra "a" entre las posiciones 0 y 12"""


m = "juan jose es un mal jefe, solo sabe exigir y no recompensar"

# a) Eliminar espacios

print(f"a) Eliminar espacios inicio y final: lo hacemos a.strip() quedando '{m.strip()}'")

# b) Convertir a mayusculas la primera letra

print(m.capitalize())

# c) Averiguar cuantos caracteres tiene, y encontrar la primera posicion de la letra "a"
print(len(m.find("a")))

# d) Contar cuantas veces aparece la letra "a" entre las posiciones 0 y 12
m.count("a",0,12)
m[0:12]
