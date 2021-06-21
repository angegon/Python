# Funciones en python
def mensaje():
    print("Como escribir una función")
    print("De la manera correcta")
    print("")
mensaje()
mensaje()
print("--> Código fuera de función <--")
mensaje()
print("")
print("###################################")

# Con parametros y retorno
def suma(a, b):
    print(a + b)
suma(3, 5)

def resta(a, b):
    resultado = a - b
    return resultado

print(resta(5, 2))