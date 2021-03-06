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

# Coronavirus - Cases vs Days
df = pd.read_excel("Data.xlsx", sheet_name='Mexponencial')

x = ((df.iloc[:, 1]).to_numpy())
x = x-x[0]
y = ((df.iloc[:, 2]).to_numpy())

p = np.polyfit(x, np.log(y), 1)

Po = np.exp(p[1])
r = p[0]

print('Coronavirus - Cases vs Days\n', r, Po)

# Valores de y calculados del ajuste
y_ajuste = Po * np.exp(r*x)

# Dibujamos los datos experimentales
p_datos, = plt.plot(x, y, 'b.')
# Dibujamos la recta de ajuste
p_ajuste, = plt.plot(x, y_ajuste, 'r-')

plt.title('Modelo Exponencial')

plt.xlabel('Eje X')
plt.ylabel('Eje Y')

plt.legend(('Datos experimentales', 'Ajuste lineal'), loc="upper left")
plt.show()
