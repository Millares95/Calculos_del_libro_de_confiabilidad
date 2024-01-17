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
f =t*Params *(exp(-Params*t))

#! Integrate describe the time to why for fail E(ttf)
limit_sup=math.inf
limit_inf=0
E_ttf = integrate(f, (t,limit_inf,+limit_sup))
print('E_ttf =',E_ttf)

#! =Cuál es la probabilidad de que un transformador de estos falle durante el primer año?======The probability distribution function of time to failure F(t)=============
f=Params *(exp(-Params*t))
limit_sup=t
limit_inf=0
F_t = integrate(f, (t,limit_inf,+limit_sup))
print('F_t =',F_t)

#Para F(t)=F_t = 1.0 - 1.0*exp(-0.2*t)
x=1
F_1= 1.0 - 1.0*exp(-0.2*x)
print('F_1=',F_1)

#! ==Cuál es la probabilidad de que un transformador de estos falle durante los primeros cinco años?======R(10)=1-F(10)
a=10
R_t=1-(1.0 - 1.0*exp(-0.2*a))
print('R_t(10)=',R_t)