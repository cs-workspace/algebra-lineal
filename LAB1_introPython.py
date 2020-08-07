''' 
Algebra Lineal - Lab1 
Entrega: 10/7/2020
@steven_wilson
'''
from random import randint

# Ejercicio 1.

Num1 = 8
Num2 = 4

print(f'\nNum1 = {Num1} and Num2 = {Num2}')

# Ejercicio 2.

sum_variables = Num1 + Num2
resta_variables = Num1 - Num2
multi_variables = Num1 * Num2
div_variables = Num1 / Num2
pot_variables = Num1**Num2

Resultados = [
    sum_variables, resta_variables, multi_variables, div_variables,
    pot_variables
]
# print(Resultados)

# Ejercicio 3.

print(f'\nLa suma entre {Num1} y {Num2} es {Resultados[0]}')

# Ejercicio 4.

columnas = 7
filas = 7


def construir_matriz(columnas, filas):
    return [[num for num in range(0, columnas)] for filas in range(filas)]


def print_matriz(matriz):
    print()
    for fila in matriz:
        print(fila)


matriz = construir_matriz(columnas, filas)

print()
print(f'Tamano: {columnas} x {filas}')
print_matriz(matriz)

# Ejercicio 5

count = 0
for fila in matriz:
    fila[count] = randint(10, 20)
    count += 1

print_matriz(matriz)