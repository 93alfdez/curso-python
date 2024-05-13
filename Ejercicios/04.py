""" Sea un str "juan jose es un mal jefe, solo sabe exigir y no recompensar", se pide:
     a) Eliminar espacios inicio y final
     b) Convertir a mayusculas la primera letra
     c) Averiguar cuantos caracteres tiene, y encontrar la primera posicion de la letra "a"
     d) Contar cuantas veces aparece la letra "a" entre las posiciones 0 y 12"""

a = "juan jose es un mal jefe, solo sabe exigir y no recompensar"

print(f"a) Eliminar espacios inicio y final: lo hacemos a.strip() quedando: '{a.strip()}'")
print(f"b) Convertir a mayusculas la primera letra: lo hacemos a.capitalize() quedando: '{a.capitalize()}'")
print(f"c1) Averiguar cuantos caracteres tiene: lo hacemos len() quedando: {len(a)} caracteres")
print(f"c2) Averiguar primera posicion de la letra 'a': lo hacemos find() quedando: {a.find("a")} posicion")
print(f"d) Contar cuantas veces aparece la letra 'a' entre las posiciones 0 y 12: lo hacemos a.count() quedando: {a.count("a",0,12)} apariciones en la frase '{a[0:12]}' que es la definida entre los indices 0 y 12")
