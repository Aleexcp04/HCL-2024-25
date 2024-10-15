""" Este superprograma se encarga de sumar los primeros 50 números impares."""

suma = 0 #Inicializo a cero, la variable donde guardo la suma.
numero = 0 #Varible numérica para recorrer los números.

for numero in range(1,101, 2):
    suma = suma + numero

print("La suma total es: ", suma)