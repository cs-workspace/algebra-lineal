# Algebra Lineal - Lab7
# Entrega: 10/7/20
# @steven_wilson

library(dplyr)
library(ggplot2)
library(readxl)
library(pracma)

#obtener datos
datos <- read_excel("Data.xlsx",sheet="Mlineal")

#ingresar arrays a funcion polyfit
p <- polyfit(datos$GRE, datos$Admision, )

#mostrar coeficientes
p

#graficar data
plot(datos$GRE, datos$Admision, pch=16, cex.lab = 1.3, col = "red", xlab="x", ylab="y", main="Recta de mejor ajuste")

#graficar recta de ajuste
yf <- polyval(p, datos$GRE)
lines(datos$GRE, yf, col="blue")