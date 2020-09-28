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




A <- matrix(c(1,2,1,  3,9,0,  1,4,-1,  4,9,3),3,4) 
A

#Encontrar el rango
RangoA <- rankMatrix(A)[1]
RangoA

#Encontrar la nulidad
nulidadA <- ncol(A)-RangoA
nulidadA

#Encontrar el espacio nulo
EspacioNuloA <- EspacioNulo(A)
EspacioNuloA
