import numpy as np
from scipy.optimize import linprog


c = np.array([-5.0, -4.0])  # Coeficientes de la funcion costo a optimizar

# Coeficientes de la matriz de desigualdades
A = np.array([[6, 4], [1, 2], [-1, 1], [0, 1]])
b = np.array([24, 6, 1, 2])  # Coeficientes libres

res = linprog(c, A, b, method="interior-point")
print("Respuesta", res)  # Mostramos la solucion completa de la funcion
# mostramos la maximizacion y sus puntos
print("Zmax es: ", res.fun*-1, " En X1:", res.x[0], " y X2:", res.x[1])
