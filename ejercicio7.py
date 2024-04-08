""" ESTO ES UN COMENTARIO, NO INFLUYE EN EL CODIGO

Nombre completo: Emiliano Fernández
Materia y curso: 6to B, D.S.I
Direccion de email: emilianofernandezesp@gmail.com """

temp1=0
temp2=0
temp3=0

temp1= int(input("Ingrese la temperatura durante la mañana: "))
temp2= int(input("Ingrese la temperatura durante la tarde: "))
temp3= int(input("Ingrese la temperatura durante la noche: "))

promedio= temp1+temp2+temp3 / 3
print("El promedio es las temperaturas ingresadas es: ",promedio)

if temp1 > promedio:
    print("La temperatura", temp1, "es mayor al promedio")
elif temp2 > promedio:
    print("La temperatura", temp2, "es mayor al promedio")
elif temp3 > promedio:
    print("La temperatura", temp3, "es mayor al promedio")