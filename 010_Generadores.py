# Estructuras que extraen valores de una función que se guardarán en objetos iterables
# Cada generador permanecera en pausa, hasta que se solicite el siguiente
# son más eficientes que las funciones tradicionales, y en determinadas condiciones en las
# que se necesita valores de uno en uno

def generaPares(Limite):
    num = 1
    miLista = []

    while num < Limite:
        miLista.append(num * 2)
        num += 1
    
    return miLista

print(generaPares(10))

# Lo mismo de antes pero generador
def generaPares(Limite):
    num = 1

    while num < Limite:
        yield num * 2
        num += 1

devuelvePares = generaPares(10)

#for i in devuelvePares:
#    print(i)

print(next(devuelvePares))
print("Aqui esta en suspensión el objeto generador")
print(next(devuelvePares))
print("Aqui esta en suspensión el objeto generador")
print(next(devuelvePares))

# 'yield from' Simplifica el código de los generadores en el caso de 
# utilizar bucles anidados

def devuelve_ciudades(*ciudades): 
    # el asterisco delante del argumento de la función, indica un número  indeterminado de argumentos en forma de tupla
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento  # Devuelve los caracteres de Madrid, etc..
        # yield elemento

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))


def devuelve_ciudades(*ciudades): 
    # el asterisco delante del argumento de la función, indica un número  indeterminado de argumentos en forma de tupla
    for elemento in ciudades:
        yield from elemento  # Devuelve los caracteres de Madrid, etc.. Sin usar dos bucles anidados como antes

ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

