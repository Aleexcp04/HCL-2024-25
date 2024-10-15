"""Programa que pide por teclado 2 numeros y diga cuál es mayor"""

#Declaracion de variables;

primerNumero = 0
segundoNumero = 0

#Programa principal:

primerNumero = float(input("Teclea el primer numero: "))
segundoNumero = float(input("Teclea el segundo numero: "))

if primerNumero > segundoNumero:
    print(f"El primer numero, que es {primerNumero}, es MAYOR que el segundo, {segundoNumero}")
else:
    if primerNumero == segundoNumero:
        print(f"El primer numero, que es {primerNumero}, es IGUAL que el segundo, {segundoNumero}")
    else:
        print(f"El primer numero, que es {primerNumero}, es MENOR que el segundo, {segundoNumero}")


"""OTRA FORMA DE HACERLO MAS RESUMIDA: 

if primerNumero > segundoNumero:
    print(f"El primer numero, que es {primerNumero}, es MAYOR que el segundo, {segundoNumero}")
elif primerNumero == segundoNumero:
        print(f"El primer numero, que es {primerNumero}, es IGUAL que el segundo, {segundoNumero}")
else:
        print(f"El primer numero, que es {primerNumero}, es MENOR que el segundo, {segundoNumero}") """
