library(dplyr)
library(ggplot2)
library(readxl)
library(pracma)

#obtener datos
datos <- read_excel("Datos.xlsx",sheet="Exponencial")
datos$Year=datos$Year-datos$Year[1]
#ingresar arrays a funcion polyfit
p <- polyfit(datos$Year, log(datos$Population), 1)

#mostrar coeficientes
r<-p[1]
Po<-exp(p[2])
r
Po

#graficar data
plot(datos$Year, datos$Population, pch=16, cex.lab = 1.3, col = "red", xlab="x", ylab="y", main="Modelo exponencial")

#graficar Modelo Exponencial
yf <- Po * exp(r*datos$Year)
lines(datos$Year, yf, col="blue")