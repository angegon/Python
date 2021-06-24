# for
for i in [1, 2, 3]:
    print("Hola")

# for sin saltos de líneas
for i in ["php", "mysql", "bbdd"]:
    print("hola", end=" ")

# for que imprime tantas veces como caracteres hay
for i in "angegon@gmail.com":
    print("hola", end=" ")

contador = 0
miEmail = input("\nPor favor, introduce tu email: ")
for i in miEmail:
    if (i == "@" or i == "."):
        contador += 1
        
if contador >= 2:
    print("\nEl email es correcto")

# for con range, se puede usar con len(variable)
for i in range(5):
    print("Hola", end=" ")
    print(i)

for i in range(5, 10):  
    print("Hola", end=" ")
    print(i)

for i in range(5, 50, 3):  # un rango de 5 a 50 e incrementa de 3 en 3
    print("Hola", end=" ")
    print(i)

# formateo 

for i in range(5):
    print(f"valor de la variable {i}")