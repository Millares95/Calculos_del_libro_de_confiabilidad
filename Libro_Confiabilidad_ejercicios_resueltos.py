 #TODO ==================Ejemplo===3.2=======================
 #! =======library==========================
from sympy import symbols ,integrate,exp
import numpy as np
from scipy.optimize import fmin
import math
#! ===============================Declare Variable=========================
Params=0.2
t=symbols('t')

#! ====Cuál es el tiempo esperado para falla?========================Integral function  E(ttf) ==========================
f =Params *(exp(-Params*t)) #Funcion distribucion exponencial

#! Integrate describe the time to why for fail E(ttf)
limit_sup=math.inf
limit_inf=0
E_ttf = integrate(t*f, (t,limit_inf,+limit_sup))
print('E_ttf =',E_ttf)

#! =Cuál es la probabilidad de que un transformador de estos falle durante el primer año?======The probability distribution function of time to failure F(t)=============
limit_sup=t
limit_inf=0
F_t = integrate(f, (t,limit_inf,+limit_sup))
print('F_t =',F_t)

#Para F(t)=F_t = 1.0 - 1.0*exp(-0.2*t)
x=1
F_1= 1.0 - 1.0*exp(-0.2*x)
print('F_1=',F_1)

#! #! Cuál es la probabilidad de que un transformador de estos NO falle durante los primeros 10 años?
z=10
R_t=1-(1.0 - 1.0*exp(-0.2*z))
print('R_t(10)=',R_t)

#TODO ==================Ejemplo===3.3======================Un componente tiene una función de vida uniformemente distribuida durante un tiempo de vida máximo  de 2400 horas=
#! Cuál es el tiempo esperado para falla 

# Distribución Uniforme.
limit_sup=2400  # En el caso de una probabilidad uniforme el infinito es la constate del mayor valor 
limit_inf=0
a=0 #tiempo inicial 
b=2400 #tiempo final 
u_t=1/(b-a) #Distribucion Uniforme 
E_ttf_u = integrate(t*u_t, (t,limit_inf,+limit_sup))
print('E_ttf_u =',E_ttf_u)

#! Cuál es la probabilidad de que un componente de estos falle durante las primeras 1200 horas?
limit_sup=t
limit_inf=0
F_t_u = integrate(u_t, (t,limit_inf,+limit_sup))
print('F_t_u =',F_t_u)

#Para F(t)=F_t_u =0.000416666666666667*t
x=1200
F_1200_u= 0.000416666666666667*x
print('F_1200_u=',F_1200_u)