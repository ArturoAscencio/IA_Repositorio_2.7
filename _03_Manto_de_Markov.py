# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

P(A ? A) = 0.6
P(A ? B) = 0.3
P(A ? C) = 0.1

P(B ? A) = 0.2
P(B ? B) = 0.5
P(B ? C) = 0.3

P(C ? A) = 0.4
P(C ? B) = 0.2
P(C ? C) = 0.4

import random

# Definir estados y matriz de transici�n
estados = ['A', 'B', 'C']
transiciones = {
    'A': {'A': 0.6, 'B': 0.3, 'C': 0.1},
    'B': {'A': 0.2, 'B': 0.5, 'C': 0.3},
    'C': {'A': 0.4, 'B': 0.2, 'C': 0.4}
}

# Estado inicial
estado_actual = 'A'

# N�mero de pasos
num_pasos = 10

# Simulaci�n de la cadena de Markov
secuencia_estados = [estado_actual]
for _ in range(num_pasos):
    # Elegir el pr�ximo estado de acuerdo con las probabilidades de transici�n
    estado_siguiente = random.choices(estados, weights=transiciones[estado_actual].values())[0]
    secuencia_estados.append(estado_siguiente)
    estado_actual = estado_siguiente

# Imprimir la secuencia de estados
print("Secuencia de Estados:")
print(" -> ".join(secuencia_estados))
