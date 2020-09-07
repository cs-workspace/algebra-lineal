""" 
Algebra Lineal
Entrega: 9/7/2020
@steven_wilson
"""

import numpy as np
from scipy.optimize import linprog


# Ejercicio 1: Maximizar utilidad de lamparas

# coeficientes de la funcion de costo a optimizar
funcion_costo = np.array([-15, -10])

# coeficientes de la matriz de desigualdades
matriz_desigualdades = np.array([[20, 30], [20, 10]])
coeficientes_libres = np.array([100, 80])  # coeficientes libres

resultado = linprog(funcion_costo, matriz_desigualdades,
                    coeficientes_libres, method="interior-point")

print("Resultado", resultado)
print("Z Maximo: ", resultado.fun * -1, " Valor de X: ",
      resultado.x[0], " Valor de Y: ", resultado.x[1])

#   -----------------------------------------------------------------------

# Ejercicio 2: Minimizar minimizar el costo y mantener el contenido de grasa no mayor de 25%

# coeficientes de la funcion de costo a optimizar
funcion_costo = np.array([80, 60])

# coeficientes de la matriz de desigualdades
matriz_desigualdades_mayor = np.array([[0.8, 0.68]])
coeficientes_libres_mayor = np.array([0.75])  # coeficientes libres

matriz_desigualdades_menor = np.array([[0.2, 0.32]])
coeficientes_libres_menor = np.array([0.25])  # coeficientes libres

resultado = linprog(funcion_costo, matriz_desigualdades_menor, coeficientes_libres_menor, matriz_desigualdades_mayor,
                    coeficientes_libres_mayor, method="interior-point")

print("\nResultado", resultado)
print("Z Minimo: ", resultado.fun * 1, " Valor de X: ",
      resultado.x[0], " Valor de Y: ", resultado.x[1])
