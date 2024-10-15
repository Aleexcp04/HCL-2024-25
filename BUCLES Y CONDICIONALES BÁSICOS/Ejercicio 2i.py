"""Programa para que pida por teclado números, hasta que introduzca el 0. Posteriormente debe mostrar su suma y su producto."""

#Declaracion de variables:

numero = 1 #Valor nnumerico que voy a pedir por teclado.
suma = 0 #Contempla la suma de todos los valores metidos por teclado.
producto = 1 # Debe almacenar la multiplicación de todos los números.

#Programa principal:

while numero != 0:
    suma = suma + numero
    producto = producto * numero
    numero = float(input("Introduce el número, porfavor (0 para terminar)"))
    """print(f"La suma da {suma} y la multiplicación {producto}")"""

print(f"La suma es {suma-1} y la multiplicación es {producto}")
