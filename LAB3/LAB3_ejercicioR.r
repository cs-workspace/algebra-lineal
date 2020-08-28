# Algebra Lineal
# Entrega: 31/8/2020
# @steven_wilson


library('pracma')


# 1. Matrices A y B tamano 15 x 15 numeros aleatorios entre (-10, 10)
A <- matrix(data = sample(-10:10, 225, TRUE), nrow = 15, ncol = 15)
print('Matriz A:')
print(A)

B <- matrix(data = sample(-10:10, 225, TRUE), nrow = 15, ncol = 15)
print('Matriz B:')
print(B)


# 2. Suma de matrices del mismo tamano
print ('Suma de matrices A + B') 
print(A + B)


# 3. Diferencia de matrices del mismo tamano
print ('Diferemcia de matrices A - B') 
print(A - B)


# 4. Producto Punto / componente por componente entre A y B.
print('Producto Componente por Componente A y B')
print(A * B)

# 5. Producto Matricial BA
print('Producto matricial BA' )
print(B %*% A) 


# 6. FERR A
print('FERR A')
rref(A)


# 7. FERR B
print('FERR B')
rref(B)