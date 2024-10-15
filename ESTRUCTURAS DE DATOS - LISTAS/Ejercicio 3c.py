"""Programa que pide introducir por teclado una matriz de 2 x 2, y nos devolverá el valor de su determinante."""

# Declaración de variables:

fila = 0 # Recorre el numero de filas de la matrix
columna = 0 # Recorre el numero de columnas de la matrix
matriz = [[0,0],[0,0]]

determinante =0

# Programa principal :

for fila in range(0,2): # Bucle que recorre las filas.
    for columna in range(0,2): # Bucle que recorre las columnas.
        matriz[fila][columna] = int(input(f"Introduce el elemento ({fila},{columna}) de la matriz: "))

determinante = matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1]

print(f"El determinante de la matriz es  {determinante}")

