""" ESTO ES UN COMENTARIO, NO INFLUYE EN EL CODIGO

Nombre completo: Emiliano Fernández
Materia y curso: 6to B, D.S.I
Direccion de email: emilianofernandezesp@gmail.com """

import random

piedra = "Piedra"
papel = "Papel"
tijera = "Tijera"

eleccion_computadora = random.choice([piedra, papel, tijera])


eleccion_usuario = input("Selecciona una opcion (Piedra, Papel, tijera): ")


if eleccion_usuario not in [piedra, papel, tijera]:
    print("Elija una opcion entre piedra, papel o tijera")
elif eleccion_usuario == eleccion_computadora:
    print("Empate")
elif eleccion_usuario == piedra and eleccion_computadora == tijera:
    print("Usted gana")
elif eleccion_usuario == papel and eleccion_computadora == piedra:
    print("Usted gana")
elif eleccion_usuario == tijera and eleccion_computadora == papel:
    print("Usted gana")
else:
    print("La computadora gano.")


print(f"Usted eligió: {eleccion_usuario}")
print(f"La computadora eligió: {eleccion_computadora}")
