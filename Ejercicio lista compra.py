"""Programa que simula una lista de compras. El programa debe permitir al usuario realizar las siguientes operaciones:
1. Agregar un artículo a la lista de compras.
2. Eliminar un artículo de la lista de compras.
3. Mostrar los artículos que están actualmente en la lista.
4. Salir del programa."""

from os import system

# Declaración de variables:
listaCompra = [] # Lista que contendrá los artículos.
opcion = 0 # Contendrá el valor elegido por el usuario en el menú.
articulo = "" # Contendrá el texto correspondiente 

# Programa principal: 

while opcion != 4:
    system("cls")
    print("") # Salto para dejar una lista en blanco.
    print("*********************       MENÚ PRINCIPAL      ***********************")
    print("1. Agregar un artículo a la lista de compras.")
    print("2. Eliminar un artículo de la lista de compras.")
    print("3. Mostrar los artículos que están actualmente en la lista.")
    print("4. Salir del programa.")
    print("")
    opcion = int(input("Elige la opción correspondiente... "))

    
    if opcion == 1: # Añadir un elemento a la lista.
        print("")
        articulo = input("Teclea un nuevo artículo para la lista de la compra: ")
        articulo = articulo.capitalize()
        if articulo in listaCompra:
            print(f"El artículo '{articulo}' ya está dentro de la lista")
            input("Pulsa una tecla para continuar...")
        else:
            listaCompra.append(articulo)



    elif opcion == 2 : # Eliminar un artículo de la lista de compras.
        print("")
        articulo = input("Teclea un artículo para eliminarlo de la lista de la compra: ")
        articulo = articulo.capitalize()
        if articulo in listaCompra:
            listaCompra.remove(articulo)
            print(f"El artículo '{articulo}' ya está eliminado de la lista de la compra")
            input("Pulsa una tecla para continuar:  ")
        else:
            print(f"El artículo '{articulo}' no está en la lista de la compra")




    elif opcion == 3: #  Mostrar los artículos que están actualmente en la lista.
        print("listado de los elementos:  ")
        print(listaCompra)
        for elemento in  listaCompra:
            print(f"-{elemento}.")



        input("Pulsa una tecla para continuar:  ")

    

