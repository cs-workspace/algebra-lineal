
# Algebra Lineal - Lab 8
# Entrega: 11/2/2020
# @steven_wilson



library(matrixcalc)

#  A 
A <- matrix(c(6, -1, 2, 3), 2, 2, byrow=TRUE)
A

ev <- eigen(A)

#eigenvalores
EIG <- ev$values
EIG

#eigenvectores
EIGV <- ev$vectors
EIGV

#diagonalizacion
P <- eigen(A)$vectors
P

D <- diag(eigen(A)$values)
D

#potencia
potencia=10

# A ^ potencia mediante diagonalizacion
Apot1 <- P %*% matrix.power(D,potencia) %*% solve(P)
Apot1

# A ^ potencia usando la funcion matrix power
Apot2 <-  matrix.power(A,potencia) 
Apot2


# B 
B <- matrix(c(2, 0, 0, 1, 2, 1, -1, 0, 1), 3, 3, byrow=TRUE)
B

ev <- eigen(B)

#eigenvalores
EIG <- ev$values
EIG

#eigenvectores
EIGV <- ev$vectors
EIGV

#diagonalizacion
P <- eigen(B)$vectors
P

D <- diag(eigen(B)$values)
D

#potencia
potencia=10

# B ^ potencia mediante diagonalizacion
Apot1 <- P %*% matrix.power(D,potencia) %*% solve(P)
Apot1

# B ^ potencia usando la funcion matrix power
Apot2 <-  matrix.power(B,potencia) 
Apot2

# C 
C <- matrix(c(1,1,0,1,1,0,1,0,0,1,0,0,0,1,0,0), 4, 4, byrow=TRUE)
C

ev <- eigen(C)

#eigenvalores
EIG <- ev$values
EIG

#eigenvectores
EIGV <- ev$vectors
EIGV

#diagonalizacion
P <- eigen(C)$vectors
P

D <- diag(eigen(C)$values)
D

#potencia
potencia=10

# C ^ potencia mediante diagonalizacion
Apot1 <- P %*% matrix.power(D,potencia) %*% solve(P, tol = 9e-18)
Apot1

# C ^ potencia usando la funcion matrix power
Apot2 <-  matrix.power(C,potencia) 
Apot2
