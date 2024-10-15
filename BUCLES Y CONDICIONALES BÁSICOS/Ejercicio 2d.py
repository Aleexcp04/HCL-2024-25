"""Programa que pide por teclado la nota de un examen y muestra por pantalla si está aprobado o suspenso (>=5)"""
#Declaracion de variables
calificacion = 0
#Programa principal.
calificacion = float(input("Introduce la cailificacion del examen: "))
if calificacion >=5:
    print(" ¡¡Estas aprobado!! ")
else:
    print(" Estas suspenso. Nos vemos el proximo año ")