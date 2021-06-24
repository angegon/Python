# Listas, pueden tener elementos iguales en posiciones diferentes
miLista = ["Angel", "Jose", "Marta", "Antonio"]

print(miLista[:]) # Imprime todos los valores de la lista
print(miLista[2])
print(miLista[-2]) # Con indices negativos, empieza a contar desde el final empezando por indice -1

### Para acceder a una porción de la lista

print(miLista[0:3]) # Imprime de indice a indice, excluyendo el último
print(miLista[:3])  # Lo mismo que el anterio pero abreviado

print(miLista[1:2])

print(miLista[1:])

### Agregar Elementos a un Lista en python y otras operaciones

miLista.append("Sandra")  #  Agregar al final
print(miLista[:])

miLista.insert(2, "Lola") # Agregar en un indice
print(miLista[:])

miLista.extend(["Juana", "Clarisa"]) # Agrega varios elementos al final
print(miLista[:])

print(miLista.index("Sandra"))  # Para saber el indice de un elemento de la lista

print("Sandra" in miLista)  # Devuelve true o false si el elemento está en la Lista

miLista.remove("Sandra") # Eliminamos elemento de la lista
print(miLista[:])

miLista.pop()  #Elimina el último elemento
print(miLista[:])


miLista = ["Maria", 5, True, 78.35]
miLista2 = ["Sandra", "Lucia"]

miLista3 = miLista + miLista2  # Concatena Listas
print(miLista3)

miLista4 = miLista3 * 3 # Multiplica la lista por n
print(miLista4)