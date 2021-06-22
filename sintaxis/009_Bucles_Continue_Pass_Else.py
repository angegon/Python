# Continue, pass y else
for letra in "Python":
    if letra == "h":
        continue

    print("Viendo la letra: " + letra)

# Contando el número de caracteres 
nombre = "Informática del futuro"
contador = 0

for i in nombre:
    if i == " ":
        continue
    contador += 1

print(len(nombre))

# Pass
while True:
    pass   # Solo se pararía con ctrl+z

class MiClase:
    pass # para implementar más tarde

# Else
email = input("Introduce tu email, por favor: ")

for i in email:
    if i == "@":
        arroba = True
        break;
else:
    arroba = False

print(arroba)