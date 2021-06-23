# Conceptos de POO, objeto estado, propiedades y comportamiento
class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False # Por defecto al crear el objeto, los coches estarán parados

    def arrancar(self): # self hacer referencia al propio objeto perteneciente a la clase, similar a this
        # pass   No hace nada, solo evita fallos de ejecución
        self.enMarcha = True
    def estado(self):
        if (self.enMarcha):
            return "El Coche está en marcha."
        else:
            return "El coche está parado."

# instanciar una clase para crear un objeto
miCoche = Coche()

# Acceder a las propiedades del objeto y cambiarlas, o acceder a los métodos

print("El largo de mi coche es: ", miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")

miCoche.arrancar()
print(miCoche.estado())

print("----------------- Creamos un segundo objeto ------------------")
miCoche2 = Coche()

print("El largo de mi coche es: ", miCoche2.largoChasis)
print("El coche tiene ", miCoche2.ruedas, " ruedas")

#miCoche2.arrancar()
print(miCoche2.estado())