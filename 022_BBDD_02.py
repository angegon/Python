import sqlite3

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()

# Para varias líneas usamos las '''
# miCursor.execute('''
#     CREATE TABLE PRODUCTOS (
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
#         PRECIO INTEGER,
#         SECCION VARCHAR(20)
#     )
# ''')

productos = [
    ("pelota", 20, "juguetería"),
    ("pantalón", 15, "confección"),
    ("destornillador", 25, "ferretería"),
    ("jarrón", 45, "cerámica")
]

# Ponemos null para la primary key
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL, ? , ? , ?)", productos)


miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confección'")
listaProductos = miCursor.fetchall()  # Los guardamos en una lista
print(listaProductos)

# Update
miCursor.execute("UPDATE PRODUCTOS SET PRECIO = '35' WHERE NOMBRE_ARTICULO = 'pelota'")

miCursor.execute("SELECT * FROM PRODUCTOS WHERE NOMBRE_ARTICULO = 'pelota'")
listaProductos = miCursor.fetchall()  # Los guardamos en una lista
print(listaProductos)

# Delete
miCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_ARTICULO = 'pelota'")

miCursor.execute("SELECT * FROM PRODUCTOS")
listaProductos = miCursor.fetchall()  # Los guardamos en una lista
print(listaProductos)


miConexion.commit()

miConexion.close()