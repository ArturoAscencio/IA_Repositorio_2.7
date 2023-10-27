# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install pgmpy

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir la estructura de la red bayesiana
model = BayesianNetwork([('Nubes', 'Lluvia'), ('Tr�fico', 'Lluvia')])

# Definir las tablas de probabilidad condicional (CPDs)
cpd_nubes = TabularCPD(variable='Nubes', variable_card=2, values=[[0.5], [0.5]])
cpd_tr�fico = TabularCPD(variable='Tr�fico', variable_card=2, values=[[0.7], [0.3]])
cpd_lluvia = TabularCPD(variable='Lluvia', variable_card=2, 
                       values=[[0.8, 0.6, 0.7, 0.1], [0.2, 0.4, 0.3, 0.9]],
                       evidence=['Nubes', 'Tr�fico'], evidence_card=[2, 2])

# Agregar las CPDs al modelo
model.add_cpds(cpd_nubes, cpd_tr�fico, cpd_lluvia)

# Verificar si el modelo es v�lido
model.check_model()

# Realizar inferencia con eliminaci�n de variables
inference = VariableElimination(model)
resultado = inference.query(variables=['Lluvia'], evidence={'Nubes': 1, 'Tr�fico': 0})

print(resultado)
