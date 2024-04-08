""" ESTO ES UN COMENTARIO, NO INFLUYE EN EL CODIGO

Nombre completo: Emiliano Fernández
Materia y curso: 6to B, D.S.I
Direccion de email: emilianofernandezesp@gmail.com """

edad1= 0
edad2=0
edad3=0
edad_min=0

edad_min=int(input("Ingrese la edad minima para poder participar: "))
edad1=int(input("Ingrese la edad del primer participante: "))
edad2=int(input("Ingrese la edad del segundo participante: "))
edad3=int(input("Ingrese la edad del tercer participante: "))

if edad1 >= edad_min and edad3 >= edad_min and edad3 >= edad_min:
    print("Todos los participantes cumplen con la edad minima")
else:
    print("Un participante no cumple con la edad minima")