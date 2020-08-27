library('pracma')

x = rbind(c(1, 2, 3))           # Vector Fila 1 x 3
print("array x")
print(x)
y = seq(0, 4, by=1)                 # Vector Fila 1 x 5 (0 al 4)
print("array y")
print(y)
z = matrix(0, 2, 3)          # Matriz cero de 2x3
print("array z ")
print(z)


s <- matrix(data = sample.int(25, 1000, TRUE), nrow = 5, ncol = 5)  #matriz de 5x5 con valores enteros aleatorios con maximo de 10-1
print("matriz s:")
print(s)

A <- matrix(c(2,3,-2,1,2,2),3,2)  #matriz 3x2
#suma de matrices
print("matriz A " )
print(A)
print ("suma A+A ") 
print(A+A)

#producto por un escalar
print("matriz 3*A ")  
print(3*A)
#negativo de una matriz
print("matriz -A ")
print(-A)


a <- matrix(c(1,0,2,-1),1,4) 
b <- matrix(c(1,0,2,-1),4,1) 

#punto elemento a elemento
print("producto elemento a elemento a*a ") 
print(a*a)



A <- matrix(c(1,0,2,2,3,-1,4,0,2),3,3) 
B <- matrix(c(1,0,2,2,3,-1,4,0,2),3,3) 

#Producto Matricial
print("producto matricial  AB  " ) 
print(A%*%B)


#Forma escalonada
A <- matrix(c(1,4,7,2,5,8,3,4,6),3,3) 

print("A: \n " )
print(A)

print("A Forma escalonada reducida: ")
rref(A)

