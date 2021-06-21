# No hay ; en el fin de línea en python
print ("Hola Mundo")

# Práctica no recomendable, más de una instrucción en una línea
print ("Hola Ángel"); print("Adios")

# Para separar una instrucción en varias líneas usamos "\"
mi_nombre = "mi nombre es Juan!"
mi_nombre = "Mi nombre es\
 Juan"
print(mi_nombre)

# El tipo de la variable lo define el contenido, en python todo son objetos
numero = 5
print(type(numero))

mensaje = """Esto es un mensaje
    con tres saltos
    de línea"""
print(mensaje)

# Operadores de comparación
if 2 < 3:
    print("true")
else:
    print("false")