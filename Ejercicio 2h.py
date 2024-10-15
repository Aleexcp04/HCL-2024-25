"""Programa para que sume todos los números pares positivos, partiendo desde 0, hasta que la suma supere el valor de 1000. Posteriormente, debe mostrar en pantalla cuál es el valor de la suma y cuántos números se han sumado."""

#Declaracion de variables:

suma = 0 #Donde guardo la suma.
numeroPar = 0 #Variable que utilizo para incrementar de 2 en 2.
contador = 0 #Variable que contará el numero de valores que sumo.

while suma <= 1000:
    contador = contador + 1
    numeroPar = numeroPar + 2
    suma = suma + numeroPar
    print(f"He sumado {contador}, que esta en el orden {contador}, y la suma es {suma}")

print(f"He sumado {contador} numero pares, y el total de la suma es {suma}")
