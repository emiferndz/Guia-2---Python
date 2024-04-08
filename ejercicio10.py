""" ESTO ES UN COMENTARIO, NO INFLUYE EN EL CODIGO

Nombre completo: Emiliano Fernández
Materia y curso: 6to B, D.S.I
Direccion de email: emilianofernandezesp@gmail.com """

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura**2)

condicion = "Obesidad" if imc >= 30 else "Sobrepeso" if imc >= 24.5 else "Peso saludable" if imc >= 18.5 else "Peso insuficiente"

peso_ideal = 21.7 * (altura**2)

print("Su IMC es de: ",imc)
print("Su condición física es: ",condicion)
print("Su peso ideal sería de: ",peso_ideal)

