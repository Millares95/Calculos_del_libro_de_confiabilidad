 #TODO ==================Ejemplo===3.2=======================
 #! =======library==========================
from sympy import symbols ,integrate,exp
import numpy as np
from scipy.optimize import fmin
import math
#! ===============================Declare Variable=========================
Parm_exp=0.2
t=symbols('t')

#! ====Cuál es el tiempo esperado para falla?========================Integral function  E(ttf) ==========================
f_exp =Parm_exp *(exp(-Parm_exp*t)) #Funcion distribucion exponencial

#! Integrate describe the time to why for fail E(ttf)
limit_sup=math.inf
limit_inf=0
E_ttf_exp = integrate(t*f_exp, (t,limit_inf,+limit_sup))
print('E_ttf_exp =',E_ttf_exp)

#! =Cuál es la probabilidad de que un transformador de estos falle durante el primer año?======The probability distribution function of time to failure F(t)=============
limit_sup=t
limit_inf=0
F_t_exp = integrate(f_exp, (t,limit_inf,+limit_sup))
print('F_t_exp =',F_t_exp)

#Para F(t)=F_t = 1.0 - 1.0*exp(-0.2*t)
x=1
F_1_exp= 1.0 - 1.0*exp(-0.2*x)
print('F_1_exp=',F_1_exp)

#! #! Cuál es la probabilidad de que un transformador de estos NO falle durante los primeros 10 años?
z=10
R_t_exp=1-(1.0 - 1.0*exp(-0.2*z))
print('R_t_exp(10)=',R_t_exp)

#TODO ==================Ejemplo===3.3======================Un componente tiene una función de vida uniformemente distribuida durante un tiempo de vida máximo  de 2400 horas=
#! Cuál es el tiempo esperado para falla 

# Distribución Uniforme.
limit_sup=2400  # En el caso de una probabilidad uniforme el infinito es la constate del mayor valor 
limit_inf=0
a=0 #tiempo inicial 
b=2400 #tiempo final 
f_u=1/(b-a) #Distribucion Uniforme 
E_ttf_u = integrate(t*f_u, (t,limit_inf,+limit_sup))
print('E_ttf_u =',E_ttf_u)

#! Cuál es la probabilidad de que un componente de estos falle durante las primeras 1200 horas?
limit_sup=t
limit_inf=0
F_t_u = integrate(f_u, (t,limit_inf,+limit_sup))
print('F_t_u =',F_t_u)

#Para F(t)=F_t_u =0.000416666666666667*t
x=1200
F_1200_u= 0.000416666666666667*x
print('F_1200_u=',F_1200_u)


#TODO =====Ejemplo3.4========La función de vida de una batería es la distribución Weibull con parámetros  0.1 α = horas y  0.5 β = .
#!Cuál es el vida esperada de esta batería?
alfa_w=0.1
beta_w=0.5
f_w=alfa_w*beta_w*(t**(beta_w-1))*(exp(-alfa_w*t**beta_w))
#Distribución Weibull
limit_sup=math.inf
limit_inf=0
E_ttf_w = integrate(t*f_w, (t,limit_inf,+limit_sup))
print('E_ttf_w =',E_ttf_w)