# Se usan para agrupar módulos relacionados entre si
# Se crean dentro de una carpeta que debe conntener u archivo __init__.py
# Es posible crear subpaquetes dentro de otros

from paquete.calculos_generales import Potencia

from paquete.basico.operaciones_basicas import *

Dividir(4, 6) # Lo toma de paquete.basico.operaciones_basicas

Potencia(4,6) 