""" ESTO ES UN COMENTARIO, NO INFLUYE EN EL CODIGO

Nombre completo: Emiliano Fernández
Materia y curso: 6to B, D.S.I
Direccion de email: emilianofernandezesp@gmail.com """

def calcular_impuestos(modelo, tipo):

  antiguedad = 2024 - modelo

  impuestos_base = 0

  if tipo == "P":
    if antiguedad < 10:
      impuestos_base = 2000
    elif antiguedad < 20:
      impuestos_base = 1500
  elif tipo == "T":
    impuestos_base = calcular_impuestos(modelo, "P") + 1500
  elif tipo == "R":
    impuestos_base = antiguedad * 1000

  return impuestos_base

modelo = int(input("Ingrese el año de fabricacion del auto: "))
tipo = input("Ingrese el tipo de auto (P/T/R): ")

impuestos = calcular_impuestos(modelo, tipo)

print("Los impuestos a pagar son: $",impuestos)
