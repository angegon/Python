# Herencia Super
class Persona():
    # constructor
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    # Métodos
    def descripcion(self):
        print("\nNombre: ", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.lugar_residencia)

class Empleado(Persona):
    # Constructor
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) # Llama al constructor de la superclase
        self.salario = salario
        self.antiguedad = antiguedad

    # Métodos
    def descripcion(self):
        super().descripcion()
        print("Salario: ",self.salario , "\nAntiguedad: ",self.antiguedad )

# Instanciamos

Antonio = Persona("Antonio", 55, "España")

Antonio.descripcion()

Antonio = Empleado(1500, 15, "Pepe", 32, "Paris")

Antonio.descripcion()

# Para comprobar si un objeto pertenece a una clase

print("Es Empleado: ", isinstance(Antonio, Empleado))
print("Es persona: ", isinstance(Antonio, Persona))