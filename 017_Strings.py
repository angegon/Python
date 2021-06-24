# Manipulación de cadenas
# Referencia de biblioteca http://pyspanishdoc.sourceforge.net/lib/string-methods.html

nombreUsuario = input("Introduce el nombre de usuario: ")

print("El nombre es: ", nombreUsuario.upper())
print("El nombre es: ", nombreUsuario.capitalize())

edad = input("Introduce la edad: ")

while (edad.isdigit() == False):
    print("Introduce un valor numérico")
    edad = input("Introduce la edad: ")

if (int(edad) < 18):
    print("No puede pasar por ser menor de edad.")
else:
    print("Puedes pasar, tienes la edad permitida")