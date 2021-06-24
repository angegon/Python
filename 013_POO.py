# Conceptos de POO, objeto estado, propiedades, comportamientos(métodos) y encapsulación 
# de métodos y propiedades
# La encapsulación no sige una norma, ha de ser en función de lo que necesite la lógica del programa
class Coche():
    # estado inicial con el constructor
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4  # Propiedad encapsulada no accesible desde fuera de la clase, para ello se ponen los dos guiones
        self.__enMarcha = False # Por defecto al crear el objeto, los coches estarán parados

    # Métodos
    def arrancar(self, arrancamos): # self hacer referencia al propio objeto perteneciente a la clase, similar a this
        # pass   No hace nada, solo evita fallos de ejecución
        self.__enMarcha = arrancamos
        if (self.__enMarcha):
            chequeo = self.__chequeoInterno()

        if (self.__enMarcha and chequeo):
            return "El Coche está en marcha."
        elif (self.__enMarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar"
        else:
            return "El coche está parado."

    def estado(self):
        print ("El coche tiene ", self.__ruedas, ". Un acho de" , self.__anchoChasis, " y un largo de ", self.__largoChasis)

    def __chequeoInterno(self): # método encapsulado
        print("Realizando chequeo interno....")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False
             

# instanciar una clase para crear un objeto
miCoche = Coche()

# Acceder a las propiedades del objeto y cambiarlas, o acceder a los métodos

#print("El largo de mi coche es: ", miCoche.largoChasis)
#print("El coche tiene ", miCoche.ruedas, " ruedas")

print(miCoche.arrancar(True))
miCoche.estado()

print("----------------- Creamos un segundo objeto ------------------")
miCoche2 = Coche()

#print("El largo de mi coche es: ", miCoche2.largoChasis)
#print("El coche tiene ", miCoche2.ruedas, " ruedas")

print(miCoche2.arrancar(False))
miCoche2.ruedas = 5  # como la propiedad está encapsulada, no es accesible desde fuera de la clase
miCoche2.estado()