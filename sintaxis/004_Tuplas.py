# Tuplas, son lista inmutables, es decir no permiten ni añadir, eliminar, modificar ni mover
# Permiten extraer porciones, dando lugar a una porción nueva.
# Son más rápidas que las listas, ocupan menos espacio, formatean strings, y pueden utilizarse
# como claves en un diccionario(las listas no).
# Se pueden realizar busquedas

mitupla = ("Angel", 13, 1, 1995) # Se declaran con parentesis(aunque son opcionales), las listas con corchetes

print(mitupla[2])

# Para convertir una tupla en una lista

print(mitupla)
milista = list(mitupla)
print(milista)

# Convertir una lista en tupla

mitupla2 = tuple(milista)
print(mitupla2)

print("Juan" in mitupla2) # true si encuentra, false sino

print(mitupla2.count("Juan")) # cuenta los elementos de la tupla que le indiquemos

print(len(mitupla2)) # cuenta los elementos de la tupla

# Declaración de tuplas unitarias

mitupla = ("Juan", )
print(len(mitupla)) 

mitupla2 = "Angel",
print(len(mitupla2))

# Asignación de variables a cada elemento de la tupla, y posterior desempaquetado de tupla
mitupla = "Angel", 13, 15
nombre, dia, numero = mitupla
print(nombre)
print(dia)
print(numero)