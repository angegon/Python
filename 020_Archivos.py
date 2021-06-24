# Manejo de archivos
# Importamos io
from io import open

# Abrimos modo escritura
archivo_texto = open("archivo.txt", "w")
frase = "Estupendo día para estudiar python \n enhorabuena!!"
# Escribimos
archivo_texto.write(frase)
# Cerramos
archivo_texto.close()

# Modo Lectura
archivo_texto = open("archivo.txt", "r")
texto = archivo_texto.read()
print(texto)
archivo_texto.close()

archivo_texto = open("archivo.txt", "r")
lineas_texto= archivo_texto.readlines()  # En este caso el resultado lo guarda en una lista
print(lineas_texto)
print(lineas_texto[0])
print(lineas_texto[1])
archivo_texto.close()

# Modo Agregar
archivo_texto = open("archivo.txt", "a")
frase = "\n Siempre es una buena ocasión para estudiar python!!"
archivo_texto.write(frase)
archivo_texto.close()

# Situar el cursos en el fichero en una posición determinada
archivo_texto = open("archivo.txt", "r")

archivo_texto.seek(11)  # Situa el cursor en el  caracter 10
print(archivo_texto.read())
archivo_texto.seek(0)
print(archivo_texto.read(11)) # Lee los primeros 11 caracteres, y deja el cursor en esa posición
print(archivo_texto.read())   # en la siguiente lectura lee a partir de la posición 10
archivo_texto.close()

# Modo leer y escribir
archivo_texto = open("archivo.txt", "r+")
