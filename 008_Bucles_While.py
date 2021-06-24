# bucle while

edad = int(input("Introduce tu edad por favor: "))

while edad < 5 or edad > 100:
    print("Has introducido una edad incorrecta. Vuelve a intentarlo")
    edad = int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar. Puedes pasar.")
print("Edad del aspirante: " + str(edad))

# Otro ejercicio con while
import math 

print("Programa de cálculo de raiz cuadrada")
numero = int(input("Introduce un número por favor: "))

intentos = 0

while numero < 0:
    print("No se puede hallar la raiz de un número negativo")

    if intentos == 2:
        print("Has consumido demasiados intentos. El programa ha finalizado.")
        break;
    
    numero = int(input("Introduce un número por favor: "))
    if numero < 0:
        intentos = intentos + 1

if intentos < 2: 
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))