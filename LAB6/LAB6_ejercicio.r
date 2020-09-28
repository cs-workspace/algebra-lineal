# Algebra Lineal - Lab6
# Entrega: 9/28/2020
# @steven_wilson

require(Matrix)
require(pracma)

#Funcion para generar el espacio nulo
EspacioNulo <- function (A) {
  m <- dim(A)[1]; n <- dim(A)[2]
  QR <- base::qr.default(A)
  r <- QR$rank
  if ((r < min(m, n)) || (m < n)) {
    R <- QR$qr[1:r, , drop = FALSE]
    P <- QR$pivot
    F <- R[, (r + 1):n, drop = FALSE]
    I <- base::diag(1, n - r)
    B <- -1.0 * base::backsolve(R, F, r)
    Y <- base::rbind(B, I)
    X <- Y[base::order(P), , drop = FALSE]
    return(X)
  }
  return(base::matrix(0, n, 1))
}




A <- matrix(c(1,1,  0,1, -1,1),2,3) 
A

B <- matrix(c(1,1,1,  1,5,-1,  -1,1,-2),3,3) 
B

C <- matrix(c(1,0,0,  1,1,1,  0,-1,-1, 1,1,-1),3,4) 
C

D <- matrix(c(2,-1,1, -4,2,-2, 0,1,1, 2,2,4, 1,3,4),3,5) 
D

#Encontrar el rango
RangoA <- rankMatrix(A)[1]
RangoA

RangoB <- rankMatrix(B)[1]
RangoB

RangoC <- rankMatrix(C)[1]
C

RangoD <- rankMatrix(D)[1]
RangoD

#Encontrar la nulidad
nulidadA <- ncol(A)-RangoA
nulidadA

nulidadB <- ncol(B)-RangoA
nulidadB

nulidadC <- ncol(C)-RangoA
nulidadC

nulidadD <- ncol(D)-RangoA
nulidadD

#Encontrar el espacio nulo
EspacioNuloA <- EspacioNulo(A)
EspacioNuloA

EspacioNuloB <- EspacioNulo(B)
EspacioNuloB

EspacioNuloC <- EspacioNulo(C)
EspacioNuloC

EspacioNuloD <- EspacioNulo(D)
EspacioNuloD
