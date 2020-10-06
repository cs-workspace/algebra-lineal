"""
Algebra Lineal Lab-7
Entrega: 10/7/20
@steven_wilson
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

# Position - Level vs Salary
df = pd.read_excel("ejercicio/Data.xlsx", sheet_name='Mcuadratico')

x = ((df.iloc[:, 1]).to_numpy())
y = ((df.iloc[:, 2]).to_numpy())

p = np.polyfit(x, y, 2)

print('Position - Cuadratic Model\n', p)


# Valores de y calculados del ajuste
y_ajuste = p[0]*x*x + p[1]*x + p[2]

# Dibujamos los datos experimentales
p_datos, = plt.plot(x, y, 'b.')
# Dibujamos la recta de ajuste
p_ajuste, = plt.plot(x, y_ajuste, 'r-')

plt.title('Parabola de mejor ajuste')

plt.xlabel('Eje X')
plt.ylabel('Eje Y')

plt.legend(('Datos experimentales', 'Ajuste lineal'), loc="upper left")
plt.show()
