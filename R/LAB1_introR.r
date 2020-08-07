# Algebra Lineal
# Entrega: 10/8/12
# @steven_wilson

# Ejercicio 1 

Num1 = 12
Num2 = 8 

sprintf('Num1 =  %i y Num2 %i', Num1, Num2)

# Ejercicio 2 

Resultados = c(Num1 + Num2, Num1 - Num2, Num1 * Num2, Num1 / Num2, Num1 ** Num2 )
print(Resultados)

# Ejercicio 3
sprintf('La suma entre %i y Num2 %i es %i', Num1, Num2, Resultados[1])
sprintf('La resta entre %i y Num2 %i es %i', Num1, Num2, Resultados[2])
sprintf('La multiplicacion entre %i y Num2 %i es %i', Num1, Num2, Resultados[3])
sprintf('La division entre %i y Num2 %i es %f', Num1, Num2, Resultados[4])
sprintf('La potencia de %i ^ %i es %i', Num1, Num2, Resultados[5])

# Ejercicio 4

matriz = rbind(
    c(1,2,3,4,5,6,7), 
    c(1,2,3,4,5,6,7),
    c(1,2,3,4,5,6,7), 
    c(1,2,3,4,5,6,7), 
    c(1,2,3,4,5,6,7), 
    c(1,2,3,4,5,6,7),
    c(1,2,3,4,5,6,7))

count = 1  
for(row in 1:nrow(matriz)) {   
    print(matriz[count, ])
    count = count + 1
    
}

# Ejercicio 5
count = 1
for(row in 1:nrow(matriz)) {   
    matriz[count, count] = 99
    count = count + 1
    
}

count = 1
for(row in 1:nrow(matriz)) {   
    print(matriz[count, ])
    count = count + 1
    
}