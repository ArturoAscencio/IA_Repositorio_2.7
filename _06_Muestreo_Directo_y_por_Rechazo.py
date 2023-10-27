import numpy as np

# Par�metros de la distribuci�n normal
media = 0
desviacion_estandar = 1
tama�o_muestra = 100

# Generar muestras de una distribuci�n normal
muestras = np.random.normal(media, desviacion_estandar, tama�o_muestra)

# Imprimir las primeras 10 muestras
print("Muestras generadas:")
print(muestras[:10])

#Muestreo por rechazo

import numpy as np

# Funci�n de densidad de probabilidad de Cauchy
def cauchy(x, x0, gamma):
    return 1 / (np.pi * gamma * (1 + ((x - x0) / gamma) ** 2))

# Par�metros de la distribuci�n de Cauchy
x0 = 0
gamma = 1
tama�o_muestra = 1000

muestras_aceptadas = []

# Generar muestras de la distribuci�n de Cauchy utilizando el muestreo por rechazo
for _ in range(tama�o_muestra):
    propuesta = np.random.uniform(x0 - 5 * gamma, x0 + 5 * gamma)
    aceptacion = np.random.uniform(0, 1)
    if aceptacion < cauchy(propuesta, x0, gamma):
        muestras_aceptadas.append(propuesta)

# Imprimir las primeras 10 muestras aceptadas
print("Muestras generadas por rechazo:")
print(muestras_aceptadas[:10])
