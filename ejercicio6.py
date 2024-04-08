""" ESTO ES UN COMENTARIO, NO INFLUYE EN EL CODIGO

Nombre completo: Emiliano Fernández
Materia y curso: 6to B, D.S.I
Direccion de email: emilianofernandezesp@gmail.com """

import random

monto = 0
premio = 70
numeros_apostados = []

monto = int(input("Ingrese el monto que va a apostar: "))

numeros = random.sample(range(0, 99))

for i in range(3):
    numero = int(input(f"Ingrese el número {i + 1} a la cabeza: "))
    numeros_apostados.append(numero)

aciertos = 0
for numero in numeros_apostados:
    if numero in numeros:
        aciertos += 1

if aciertos > 0:
    premio_total = monto * premio * aciertos
    print(f"Felicidades, acertaste",aciertos,"número(s).")
    print(f"Su premio es de: $",premio_total)
else:
    print("Lo sentimos, no ha acertado ningun numero.")

