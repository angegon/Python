# Herencia superclase y clases hijas
class Vehiculos():
    # Constructor
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    # Métodos
    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True
    
    def estado(self):
        print("\nMarca; ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", 
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

# Clases hijas
class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if (self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo el caballito"

    # Sobrescribimmos el método estado
    def estado(self):
        print("\nMarca; ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", 
        self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

# Clase que no hereda
class VElectricos():
    def __init__(self):
        self.autonomia = "100km"
    
    def cargarEnergia(self):
        self.cargando = True

# Clase con herencia multiple, se da preferencia la primera clase que indiques
# en cuanto a constructor en la siguiente se heredaría el de constructor
class BicicletaElectrica(Vehiculos, VElectricos):
    pass

# instanciamos
miMoto = Moto("Honda", "CBR")
miFurgoneta = Furgoneta("Renault", "Kangoo")
miBici = BicicletaElectrica("Orbea", "HC1030")

# Método heredado de la superclase
miMoto.caballito() 

miMoto.estado() # Sobreescribe el método de la superclase, 

miFurgoneta.arrancar()

miFurgoneta.carga(True)

miFurgoneta.estado()

