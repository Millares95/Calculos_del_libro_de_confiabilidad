 #TODO ==================Ejemplo===3.2=======================
 #! =======library==========================
from sympy import symbols ,integrate,exp,pi,erf,sqrt
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
F_1_exp= F_t_exp.subs(t,1)#Evaluar el valor de t de la expresion resultante
print('F_1_exp=',F_1_exp)

#! #! Cuál es la probabilidad de que un transformador de estos NO falle durante los primeros 10 años?
R_t_exp=1-F_t_exp.subs(t,10)
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
F_1200_u= F_t_u.subs(t,1200)
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

#!Cuál es la probabilidad de que una batería de estas falle durante las primeras 200 horas?
limit_sup=t
limit_inf=0
F_t_w = integrate(f_w, (t,limit_inf,+limit_sup))
F_200_w =F_t_w.subs(t,200)
print('F_200_w=',F_200_w)

#! Cuál es la probabilidad de que una batería de éstas viva más de 300 horas?
R_t_w=1-F_t_w.subs(t,300)
print('R_(300)_w=',R_t_w)

#TODO =====Ejemplo3.6=====Una  persona  instala  una  cortina  de  luces  navideñas  que  consta  2000  bombillas  con  una  función  de  vida  Gausiana de valor medio 1000 horas y una desviación estándar de 200 horas.
#! Cuántas bombillas puede esperarse que fallen en las primeras 1000 horas?
media=1000
desv_stndr=200
#estadigrafo de la distribucion normal
f_N=(1 / (sqrt(2 * pi * desv_stndr**2))) * exp(-((t - media)**2) / (2 * desv_stndr**2))
limit_sup=t
limit_inf=0
F_t_N = integrate(f_N, (t,limit_inf,+limit_sup))
print('F_t_N =',F_t_N)
F_700_N =F_t_N.subs(t, 700).evalf()
print('F_700_N=',F_700_N) 
