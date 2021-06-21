# Diccionarios
# Son estructuras de datos(enteros, cadenas de texto, decimales, listas, diccionarios, etc..),
# en forma de clave:valor , la clave es única en el diccionario. Y los elementos no están ordenados.

miDiccionario = {"Alemania":"Berlin", "España":"Madrid" , "Francia":"Paris" }

print(miDiccionario["Alemania"])
print(miDiccionario)

# Agregar elementos a un diccionario
miDiccionario["Italia"] = "Lisboa"
print(miDiccionario)
miDiccionario["Italia"] = "Roma"
print(miDiccionario)

# Borrar un elemento del diccionario

del miDiccionario["Alemania"]
print(miDiccionario)

# Crear un diccionario a partir de una tupla

mitupla = ["España", "Francia", "Reino Unido", "Alemania"]
miDiccionario = {mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres", mitupla[3]:"Berlín"}
print(miDiccionario)

# Agregar a un diccionario

miDiccionario = {23:"jordan", "Nombre": "Michael", "Equipo":"Chicago", "Anillos":[1991,1992,1993]}

print(miDiccionario["Equipo"])
print(miDiccionario["Anillos"])

# Guardar un diccionario dentro de otro

miDiccionario = {23:"jordan", "Nombre": "Michael", "Equipo":"Chicago", "Anillos":{"temporadas": [1991,1992,1993]}}

print(miDiccionario["Equipo"])
print(miDiccionario["Anillos"])

# Para imprimir claves y valores
print(miDiccionario.keys())
print(miDiccionario.values())
print(len(miDiccionario))