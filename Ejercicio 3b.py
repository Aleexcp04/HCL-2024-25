"""Programa que pide por teclado la lista de los números de la lotería de los últimos 7 días. Posteriormente los mostrará ordenados de menor a mayor y de mayor a menor."""

#Declaración de variables:

numerosLoteria = [0, 0, 0, 0, 0, 0, 0]

for contador in range (0,7):
    numerosLoteria [contador] = int(input(f"Introduce el dia de la loteria del {contador}º dia  "))

numerosLoteria.sort() #Función para ordenar la lista de menor a mayor

print(f"La lista de los números de menor a mayor es: {numerosLoteria}")

numerosLoteria.sort(reverse = True) #Función para ordenar la lista de mayor a menor

print(f"La lista de los números de mayor a menor es: {numerosLoteria}")

""" (numerosLoteria).append("Lo que quiero añadir") #Añade un elemento a la lista
    (numerosLoteria).remove("Lo que quiero borrar") # Borra un elemento de la lista  """
