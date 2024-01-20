 #TODO ==================Ejemplo===3.2=======================
 #! =======library==========================
from sympy import symbols ,integrate,exp,pi,erf,sqrt,Eq,solve
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
#! Cuántas bombillas puede esperarse que fallen en las primeras 700 horas?
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
n_Bomb=2000*F_700_N
print ("n_Bomb=",round(n_Bomb))

#La probabilidad de que fallen 134 de las 2000 bombillas debe hallarse por medio de la distribución  binomial o la aproximación de la distribución Gausiana a la binomial.
#!Cuántas bombillas puede esperarse que fallen entre las 900 y 1300 horas?

F_900_N =F_t_N.subs(t, 900).evalf()
F_1300_N =F_t_N.subs(t, 1300).evalf()
F_900_N_t_F_1300_N=F_1300_N-F_900_N
print("F_900_N_t_F_1300_N=",F_900_N_t_F_1300_N)
n_Bomb=2000*F_900_N_t_F_1300_N
print ("n_Bomb=",round(n_Bomb))

#! Después de qué periodo de tiempo se espera que haya fallado el 10% de las bombillas?
Prob=0.1
equation=Eq(0.1,F_t_N)
solution=solve(equation,t)
print("se espera que haya fallado el 10% de las bombillas en",solution,"horas")

#Todo VIDA RESIDUAL  EJEMPLO 3.9==Un transformador de potencia típico tiene una función de vida Gausiana con  45 μ=  años y  10 σ = años.===
#! Si el transformador no ha fallado en los primeros 30 años, cuál es la probabilidad de que falle en los  siguientes 20 años?
# F(20)=(F(t+Delta_t)-F(t))/(1-F(t))=(F(30+20)-F(30))/(1-F(30))
media=45
desv_stndr=10 
f_N=(1 / (sqrt(2 * pi * desv_stndr**2))) * exp(-((t - media)**2) / (2 * desv_stndr**2))
F_t_N = integrate(f_N, (t,limit_inf,+limit_sup))
F_50_N =F_t_N.subs(t, 50).evalf()
F_30_N =F_t_N.subs(t, 30).evalf()
F_20_N=(F_50_N-F_30_N)/(1-F_30_N)
print('F_20_N =',F_20_N)

#! Si el transformador no ha fallado en los primeros 30 años, cuál es la probabilidad de que sobreviva 20  años más?
R_20__N_sobreviva=(1-(F_50_N))/(1-F_30_N)
print('R_20__N_sobreviva=',R_20__N_sobreviva)

#!Si el transformador no ha fallado en los primeros 40 años, cuál es la probabilidad de que falle en los  siguientes 20 año?
F_60_N =F_t_N.subs(t, 60).evalf()
F_40_N =F_t_N.subs(t, 40).evalf()
F_20_N_other=(F_60_N-F_40_N)/(1-F_40_N)
print('F_20_N_other =',F_20_N_other)

#!Si el transformador no ha fallado en los primeros 50 años, cuál es la probabilidad de que falle en los  siguientes 20 años?
F_70_N =F_t_N.subs(t, 70).evalf()
F_20_N_other1=(F_70_N-F_50_N)/(1-F_50_N)
print('F_20_N_other1 =',F_20_N_other1) 

#Todo VIDA RESIDUAL  EJEMPLO 3.10==Para  un  componente  dado  se  encuentra  que su función  de  vida es  exponencial  con  valor esperado  de 5  años.
#*Modelo de Vida
Parm_exp=5
f_exp_1=1-exp(-1/Parm_exp)
E_ttf_exp1=Parm_exp
lamda_Densidad_de_falla=1/E_ttf_exp1 #La tasa de fallas es constante, lo cual indica que el componente no presenta envejecimiento ni mejora  en su confiabilidad.

#!Si  un  componente  de  éstos  no  ha  fallado  en  3  años,  cuál  es  la  probabilidad  de  que  falle  en  los  siguientes 2 años?

limit_sup=t
limit_inf=0
F_t_exp1 = integrate(f_exp_1, (t,limit_inf,+limit_sup))
print('F_t_exp =',F_t_exp)
F_3_exp1=F_t_exp.subs(t,3).evalf()
F_5_exp1=F_t_exp.subs(t,5).evalf()
F_2_exp1=(F_5_exp1-F_3_exp1)/(1-F_3_exp1)
print("F_2_exp1=",F_2_exp1)


