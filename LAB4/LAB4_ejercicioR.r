# Algebra Lineal
# Entrega 9/7/2020
# @steven_wilson

library(boot)

# Ejercicio 1: Maximizar utilidad de lamparas

c<-c(15, 10)
A<-rbind(c(20,30),c(20,10))
b<-c(100, 80)

simplex(a=c, A1=A, b1=b, maxi="TRUE")

#   -----------------------------------------------------------------------

# Ejercicio 2: Minimizar minimizar el costo y mantener el contenido de grasa no mayor de 25%

c<-c(80, 60)
A<-rbind(c(0.8,0.68))
b<-c(0.75)

D<-rbind(c(0.2, 0.32))
e<-c(0.25)

simplex(a=c, A1=A, b1=b, A2=D, b2=e, maxi="TRUE")
