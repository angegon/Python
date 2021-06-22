# if básico
print("Pregrama de evaluación de notas de alumnos")

nota_alumno = int(input("introduce la nota del alumno: "))

def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "Suspenso"
    return valoracion

print(evaluacion(nota_alumno))

# if else elif
print("Verificación de acceso")

edad_usuario = int(input("Introduce tu edad, por favor: "))

if edad_usuario < 18:
    print("no puedes pasar")
elif edad_usuario > 100:
    print("Edad incorrecta")
else:
    print("Puedes pasar")

print("El programa ha finalizado")

# < > 
edad = -7

if 0<edad<100:
    print("Edad es correcta")
else:
    print("Edad incorrecta")

# ...and ... or 

print("Programa de becas Año 2017")
distancia_escuela = int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el nº de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar = int(input("Introduce salario anual bruto: "))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
    print("Tienes derecho a beca!")
else:
    print("No tienes derecho a beca :(")

# ... in , python es case sensitive

print("Asignaturas optativas año 2017")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion = input("Escribe la asignatura escogida: ")
asignatura = opcion.lower()

if (asignatura) in ("informática gráfica", "iruebas de software", "isabilidad y accesibilidad"):
    print("Asignatura escogida: " + opcion)
else:
    print("La asignatura escogida no está contemplada")