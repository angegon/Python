# Trabajo con base de datos sql lite, no permite usuarios
# Para ver el contenido de la bbdd podemos usar https://sqlitebrowser.org/
# importamos librería 

import sqlite3

# Abrimos la conexión, a la vez sino existe crea la bbdd
miConexion = sqlite3.connect("BBDD_01")

# Creamos el cursor o puntero
miCursor  = miConexion.cursor()

# Ejecutamos la query sql usando el cursor (CRUD)
# miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
# miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON', 15, 'DEPORTES')")

variosProductos = [
    ("Camiseta", 10, "Deportes"),
    ("Jarrón", 90,  "Ceramica"),
    ("Camión", 20, "Jugueteria")
]
# Para insertar varios elementos de una lista
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?, ? , ?)", variosProductos)

# Para Leer registros de la BBDD
miCursor.execute("SELECT * FROM PRODUCTOS")

listaProductos = miCursor.fetchall()  # Los guardamos en una lista

print(listaProductos)

for producto in listaProductos:
    print("Nombre artículo: ", producto[0], "Precio Producto: ", producto[1], "Sección Producto: ", producto[2])

# Guardamos los cambios
miConexion.commit()

# Cerramos la conexión
miConexion.close()
