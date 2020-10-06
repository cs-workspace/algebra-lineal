import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


df = pd.read_excel("Datos.xlsx", sheet_name='Cuadratico')

x = ((df.iloc[:, 0]).to_numpy())
y = ((df.iloc[:, 1]).to_numpy())

p = np.polyfit(x, y, 2)

print(p)


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
