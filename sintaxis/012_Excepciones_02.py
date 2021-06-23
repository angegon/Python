# Manejo de excepciones para errores en tiempo de ejecución
def divide():
    try:
        op1 = (float(input("Introduce el primer número: ")))
        op2 = (float(input("Introduce el segundo número: ")))
        print("La división es: " + str(op1/ op2))
    except ValueError:
        print("Los valores introducidos no son correctos. Intentalo de nuevo: ")
    except ZeroDivisionError:
        print("No se puede dividir entre 0!")
    except:
        print("Ha ocurrido un error!, excepción general")
    finally:  # siempre se ejecuta, incluso aunque no se capturen las excepciones antes
        print("Calculo finalizado.")
divide()

# Otro caso de uso con una excepción ya definida en python

def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("No se permiten edades negativas.")
    if edad < 20:
        return "eres muy joven"
    elif edad < 40:
        return "eres joven"
    elif edad < 65:
        return "eres maduro"
    elif edad < 100:
        return "eres viejuno. Cuidate..."

print(evaluaEdad(70))

# Excepciones propias, hay que definir la clase previamente de la excepción propia
def evaluaEdad(edad):
    #if edad < 0:
        #raise MiPropioError("No se permiten edades negativas.") # la excepción dara error
    if edad < 20:
        return "eres muy joven"
    elif edad < 40:
        return "eres joven"
    elif edad < 65:
        return "eres maduro"
    elif edad < 100:
        return "eres viejuno. Cuidate..."

print(evaluaEdad(70))

# Otro caso más con alia
import math

def calculaRaiz(num1):

    if num1 < 0:
        raise ValueError("El número no puede ser negativo")
    
    else: 
        return math.sqrt(num1)

opt = (int(input("Introduce un número: ")))
try:
    print(calculaRaiz(opt))
except ValueError as ErrorDeNumeroNegativo: # Alias. que tomará el texto del raise
    print(ErrorDeNumeroNegativo)

print("Programa terminado.")