from sympy import symbols, Function, dsolve, Eq
import matplotlib.pyplot as plt

# Definir variables y funciones simbólicas
t = symbols('t')
Ps, T, D, m, r = symbols('Ps T D m r')
P0, P1, P2, P3 = symbols('P0 P1 P2 P3', cls=Function)

# Definir el sistema de ecuaciones diferenciales
eq1 = Eq(P0(t).diff(t), -(((1 - Ps) / T) + (Ps / T)) * P0(t) + (1 / T) * P1(t) + (1 / r) * P3(t))
eq2 = Eq(P1(t).diff(t), -((1 / D) + (1 / r)) * P1(t) + ((1 - Ps) / T) * P0(t) + (1 / m) * P2(t))
eq3 = Eq(P2(t).diff(t), -((1 / m) + (1 / D)) * P2(t) + (Ps / T) * P0(t) + (1 / r) * P1(t) + (1 / T) * P3(t))
eq4 = Eq(P3(t).diff(t), -((1 / r) + (1 / T)) * P3(t) + ((1 / D) * P2(t)))

# Especificar condiciones iniciales en t = 0
condiciones_iniciales = {P0(0): 0, P1(0): 1, P2(0): 0, P3(0): 0}

# Resolver el sistema de ecuaciones diferenciales con condiciones iniciales
soluciones = dsolve([eq1, eq2, eq3, eq4], ics=condiciones_iniciales)
print(soluciones)
