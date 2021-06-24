# Polimorfismo: indica que un objeto puede cambiar de forma dependiendo del contexto
# en el que se utilice

class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 reudas.")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas.")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas.")

# Función polimorfica que dependiendo del tipo de objeto que reciba, llamada al metodo de una clase u otra
def desplazamientoVehiculo(Vehiculo):
    Vehiculo.desplazamiento()

miVehiculo = Moto()
miVehiculo.desplazamiento()

miVehiculo2 = Coche()
miVehiculo2.desplazamiento()

miVehiculo3 = Camion()
miVehiculo3.desplazamiento()

desplazamientoVehiculo(miVehiculo)
desplazamientoVehiculo(miVehiculo2)
desplazamientoVehiculo(miVehiculo3)