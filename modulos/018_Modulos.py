# Importamos el módulo anterior para utulizarlo, sino lo encuentra en el directorio,
# lo busca en el syspath

# Modo 1
# import funciones_matematicas
# funciones_matematicas.Restar(1, 2)

# Modo 2
from funciones_matematicas import *  # Se puede importar una sola función
Sumar(1, 2)

# Otro caso de uso
from modulo_vehiculo import *

coche = Vehiculos("Mazda", "MX5")

coche.estado()
