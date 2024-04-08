""" ESTO ES UN COMENTARIO, NO INFLUYE EN EL CODIGO

Nombre completo: Emiliano Fernández
Materia y curso: 6to B, D.S.I
Direccion de email: emilianofernandezesp@gmail.com """

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

suma= num1+num2+num3

if suma > 10:
    resultado= suma/2
else:
    resultado= suma**3
    
print("El resultado es: ", resultado)