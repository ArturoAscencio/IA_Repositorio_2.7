import numpy as np

# Funci�n objetivo (distribuci�n que queremos muestrear)
def funcion_objetivo(x):
    return np.exp(-x**2) * (4 * x**2 + 1)

# Funci�n de transici�n (propuesta)
def funcion_transicion(x):
    return x + np.random.normal(0, 0.5)

# N�mero de muestras a generar
num_muestras = 10000

# Valor inicial
x_actual = 0.0

muestras = []

for _ in range(num_muestras):
    # Generar una propuesta de transici�n
    x_propuesta = funcion_transicion(x_actual)
    
    # Calcular la raz�n de aceptaci�n
    razon_aceptacion = funcion_objetivo(x_propuesta) / funcion_objetivo(x_actual)
    
    # Aceptar o rechazar la propuesta
    if np.random.rand() < razon_aceptacion:
        x_actual = x_propuesta
    
    muestras.append(x_actual)

# Imprimir el promedio de las muestras
print("Promedio de las muestras:", np.mean(muestras))
