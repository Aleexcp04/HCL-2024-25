"""Programa (Tuplas) que pide por teclado un valor entre 1 y 7 y debe indicarnos por pantalla el día de la semana correspondiente."""

#Declaracion de variables:

diaSemana = 0 #Contiene el valor numérico del orden del dia de la semana.
nombresDias = ("LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SABADO", "DOMINGO")

#Programa principal:

diaSemana = int(input("Teclea el número del dia de la semana (1 - 7): "))

print(f"El dia de la semana es {nombresDias[diaSemana - 1]}")