library(dplyr)
library(ggplot2)
library(readxl)
library(pracma)

#obtener datos
datos <- read_excel("Datos.xlsx",sheet="Cuadratico")

#ingresar arrays a funcion polyfit
p <- polyfit(datos$cantidad, datos$Ingreso, 2)

#mostrar coeficientes
p

#graficar data
plot(datos$cantidad, datos$Ingreso, pch=16, cex.lab = 1.3, col = "red", xlab="x", ylab="y", main="Parabola de mejor ajuste")

#graficar recta de ajuste
yf <- polyval(p, datos$cantidad)
lines(datos$cantidad, yf, col="blue")