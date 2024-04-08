""" ESTO ES UN COMENTARIO, NO INFLUYE EN EL CODIGO

Nombre completo: Emiliano Fernández
Materia y curso: 6to B, D.S.I
Direccion de email: emilianofernandezesp@gmail.com """

turno = 0
horas_trabajadas = 0
valor_diurno = 350.50
valor_nocturno = 400.60

turno = int(input("Ingrese el codigo de turno (1 - Diurno, 2 - Nocturno): "))
horas_trabajadas = int(input("Ingrese las horas trabajadas: "))

if turno == 1:   
    diurno = horas_trabajadas * valor_diurno
    print("Usted cobrará",diurno, "por trabajar en horario diurno")
else:
    nocturno = horas_trabajadas * valor_nocturno
    print("Usted cobrará",nocturno, "por trabajar en horario nocturno")
