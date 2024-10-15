""" Este superprograma se encarga de sumar los primeros N números pares.""" 

#Declaracion de variables:
suma = 0 #Variable que acumula la suma de los numeros.
i = 0 #Variable indice con el que recorro el bucle.
numeroFinal = 0 #Valor igual que indica cuando acaba el bucle ( se pide por teclado )

numeroFinal = int(input("¿Cuantos valores quieres sumar?"))

for i in range(0,numeroFinal*2, 2):
    print("Numero par: ", end= " ")
    print(i)
    suma = suma + i
print("La suma total es: ", suma )