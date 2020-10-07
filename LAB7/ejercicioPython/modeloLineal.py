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

# GRE - Admission
df = pd.read_excel("Data.xlsx", sheet_name='Mlineal')

x = ((df.iloc[:, 0]).to_numpy())
y = ((df.iloc[:, 1]).to_numpy())

p = np.polyfit(x, y, 1)

print('GRE - Admission\n', p)


# Valores de y calculados del ajuste
y_ajuste = p[0]*x + p[1]

# Dibujamos los datos experimentales
p_datos, = plt.plot(x, y, 'b.')
# Dibujamos la recta de ajuste
p_ajuste, = plt.plot(x, y_ajuste, 'r-')

plt.title('Recta de mejor ajuste')

plt.xlabel('Eje X')
plt.ylabel('Eje Y')

plt.legend(('Datos experimentales', 'Ajuste lineal'), loc="upper left")
plt.show()
