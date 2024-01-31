 #TODO ==================Ejemplo===3.2=======================
 #! =======library==========================
from sympy import symbols ,integrate,exp,pi,erf,sqrt,Eq,solve
import numpy as np
from scipy.optimize import fmin
import math
t=symbols("t")

#TODO Declaracion de funciones de distribución

#! FUNCION DE DISTRIBUCION  EXPONENCIAL__________________________________________________________
def Funcion_exp(Parm_exp):
    t=symbols('t')
    f_exp =Parm_exp *(exp(-Parm_exp*t))
    return f_exp #Funcion distribucion exponencial

#! FUNCION DE DISTRIBUCION UNIFORME_____________________________________________
def Funcion_unif(a,b):
    f_u=1/(b-a)
    return f_u
#! FUNCION DE DISTRIBUCION WEIBULL_____________________________________________
def Funcion_wbll(alfa_w,beta_w):
    t=symbols('t')
    f_w=alfa_w*beta_w*(t**(beta_w-1))*(exp(-alfa_w*t**beta_w))
    return f_w

#! FUNCION DE DISTRIBUCION NORMLAL_____________________________________________
def Funcion_normal(media,desv_stndr):
    f_N=(1 / (sqrt(2 * pi * desv_stndr**2))) * exp(-((t - media)**2) / (2 * desv_stndr**2))
    return f_N
#!_______________________________________________________________________________
def Tiempo_hasta_falla(limit_inf,limit_sup,funcion):
    t=symbols('t')
    E_ttf_exp = integrate(t*funcion, (t,limit_inf,+limit_sup))
    return E_ttf_exp
def Probabilidad_de_falla_en_un_tiempo(limit_inf,limit_sup,funcion):
    t=symbols('t')
    F_t_exp = integrate(funcion, (t,limit_inf,limit_sup))
    return F_t_exp

#!_______________________________________________________________________________

#TODO EJEMPLO 3.2==================================================
#! ====Cuál es el tiempo esperado para falla?========================
print(Funcion_exp(0.2))
#! Integrate describe the time to why for fail E(ttf)
print('Tiempo hasta la falla =',Tiempo_hasta_falla(0,math.inf,Funcion_exp(0.2)))

#! =Cuál es la probabilidad de que un transformador de estos falle durante el primer año?======The probability distribution function of time to failure F(t)=============
F_t_exp=Probabilidad_de_falla_en_un_tiempo (0,symbols('t'),Funcion_exp(0.2))
F_1_exp=F_t_exp.subs({t:1})
print('F_1_exp=',F_1_exp)


# #! #! Cuál es la probabilidad de que un transformador de estos NO falle durante los primeros 10 años?
R_t_exp=1-F_t_exp.subs(t,10)
print('R_t_exp(10)=',R_t_exp)

# #TODO ==================Ejemplo===3.3======================Un componente tiene una función de vida uniformemente distribuida durante un tiempo de vida máximo  de 2400 horas=
# #! Cuál es el tiempo esperado para falla
print(Funcion_unif(0,2400))
E_ttf_u=Tiempo_hasta_falla(0,2400,Funcion_unif(0,2400))
print('E_ttf_u =',E_ttf_u)

# #! Cuál es la probabilidad de que un componente de estos falle durante las primeras 1200 horas?
F_t_u=Probabilidad_de_falla_en_un_tiempo (0,symbols('t'),Funcion_unif(0,2400))
F_1200_u=F_t_u.subs({t:1200})
print('F_1200_u=',F_1200_u)



# #TODO =====Ejemplo3.4========La función de vida de una batería es la distribución Weibull con parámetros  0.1 α = horas y  0.5 β = .
# #!Cuál es el vida esperada de esta batería?
Funcion_wbll(0.1,0.5)
E_ttf_w=Tiempo_hasta_falla(0,math.inf,Funcion_wbll(0.1,0.5))
print('E_ttf_w =',E_ttf_w)

# #!Cuál es la probabilidad de que una batería de estas falle durante las primeras 200 horas?
F_t_w=Probabilidad_de_falla_en_un_tiempo (0,symbols('t'),Funcion_wbll(0.1,0.5))
F_200_w=F_t_w.subs({t:1200})
print('F_200_w=',F_200_w)

# #! Cuál es la probabilidad de que una batería de éstas viva más de 300 horas?
R_t_w=1-F_t_w.subs(t,300)
print('R_(300)_w=',R_t_w)

# #TODO =====Ejemplo3.6=====Una  persona  instala  una  cortina  de  luces  navideñas  que  consta  2000  bombillas  con  una  función  de  vida  Gausiana de valor medio 1000 horas y una desviación estándar de 200 horas.
# #! Cuántas bombillas puede esperarse que fallen en las primeras 700 horas?
Funcion_normal(1000,200)
F_t_N= Probabilidad_de_falla_en_un_tiempo (0,symbols('t'),Funcion_normal(1000,200))
F_700_N=F_t_N.subs(t, 700).evalf()
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

# #! Después de qué periodo de tiempo se espera que haya fallado el 10% de las bombillas?
Prob=0.1
equation=Eq(0.1,F_t_N)
solution=solve(equation,t)
print("se espera que haya fallado el 10% de las bombillas en",solution,"horas")

# #Todo VIDA RESIDUAL  EJEMPLO 3.9==Un transformador de potencia típico tiene una función de vida Gausiana con  45 μ=  años y  10 σ = años.===
# #! Si el transformador no ha fallado en los primeros 30 años, cuál es la probabilidad de que falle en los  siguientes 20 años?
# F(20)=(F(t+Delta_t)-F(t))/(1-F(t))=(F(30+20)-F(30))/(1-F(30))
Funcion_normal(45,10)
F_t_N= Probabilidad_de_falla_en_un_tiempo (0,symbols('t'),Funcion_normal(45,10))
F_50_N =F_t_N.subs(t, 50).evalf()
F_30_N =F_t_N.subs(t, 30).evalf()
F_20_N=(F_50_N-F_30_N)/(1-F_30_N)
print('F_20_N =',F_20_N)

# #! Si el transformador no ha fallado en los primeros 30 años, cuál es la probabilidad de que sobreviva 20  años más?
R_20__N_sobreviva=(1-(F_50_N))/(1-F_30_N)
print('R_20__N_sobreviva=',R_20__N_sobreviva)

# #!Si el transformador no ha fallado en los primeros 40 años, cuál es la probabilidad de que falle en los  siguientes 20 año?
F_60_N =F_t_N.subs(t, 60).evalf()
F_40_N =F_t_N.subs(t, 40).evalf()
F_20_N_other=(F_60_N-F_40_N)/(1-F_40_N)
print('F_20_N_other =',F_20_N_other)

#!Si el transformador no ha fallado en los primeros 50 años, cuál es la probabilidad de que falle en los  siguientes 20 años?
F_70_N =F_t_N.subs(t, 70).evalf()
F_20_N_other1=(F_70_N-F_50_N)/(1-F_50_N)
print('F_20_N_other1 =',F_20_N_other1) 

# #Todo VIDA RESIDUAL  EJEMPLO 3.10==Para  un  componente  dado  se  encuentra  que su función  de  vida es  exponencial  con  valor esperado  de 5  años.
# #*Modelo de Vida
Parm_exp=5
f_exp_1=1-exp(-1/Parm_exp)
E_ttf_exp1=Parm_exp
lamda_Densidad_de_falla=1/E_ttf_exp1 #La tasa de fallas es constante, lo cual indica que el componente no presenta envejecimiento ni mejora  en su confiabilidad.

# #!Si  un  componente  de  éstos  no  ha  fallado  en  3  años,  cuál  es  la  probabilidad  de  que  falle  en  los  siguientes 2 años?

limit_sup=t
limit_inf=0
F_t_exp1 = integrate(f_exp_1, (t,limit_inf,+limit_sup))
print('F_t_exp =',F_t_exp)
F_3_exp1=F_t_exp.subs(t,3).evalf()
F_5_exp1=F_t_exp.subs(t,5).evalf()
F_2_exp1=(F_5_exp1-F_3_exp1)/(1-F_3_exp1)
print("F_2_exp1=",F_2_exp1)


# #Todo====== Ejemplo4.2====================
# # Todo Solucion analitica de las cadenas de Markow homogénea exponencial
# #* Para  un  transformador  de  potencia  220/115  kV,  80/100  MVA,  
# #*ONAN/ONAF  se  definen  los  siguientes  estados operativos: 
# #* Tiempos de transicion exponencial

# #? Es la tasa de fallas y reparaciones dl sistema que crean la taza de transicion

h_12=1/ (Tiempo_hasta_falla(0,math.inf,Funcion_exp(4)))
print("h_12=",h_12)
h_21=1/ (Tiempo_hasta_falla(0,math.inf,Funcion_exp(73)))
print("h_21=",h_21)
h_13=1/ (Tiempo_hasta_falla(0,math.inf,Funcion_exp(2)))
print("h_13=",h_13)
h_31=1/ (Tiempo_hasta_falla(0,math.inf,Funcion_exp(18.25)))
print("h_31=",h_31)

h_11=-(h_12+h_13)
h_23=0
h_22=-(h_21+h_23)
h_32=0
h_33=-h_31
lista=[h_11,h_12,h_13,h_21,h_22,h_23,h_31,h_32,h_33]
# Definir la matriz Markov como una matriz numpy usando la lista h
Matriz_Markov = np.array(lista).reshape((3, 3))
print("\n Matriz Markov\n",Matriz_Markov)

# Sistema de ecuaciones Diferenciales 3x3
from sympy import symbols, Function, dsolve, Eq
import matplotlib.pyplot as plt
# Definir variables y funciones simbólicas
t = symbols('t')
P1, P2, P3 = symbols('P1 P2 P3', cls=Function)

# Definir el sistema de ecuaciones diferenciales
eq1 = Eq(P1(t).diff(t), h_11*P1(t) +h_12*P2(t)+h_13*P3(t))
eq2 = Eq(P2(t).diff(t), h_21*P1(t) +h_22*P2(t)+h_23*P3(t))
eq3 = Eq(P3(t).diff(t), h_31*P1(t) +h_32*P2(t)+h_33*P3(t))

# Especificar condiciones iniciales en t = 0
condiciones_iniciales = {P1(0): 1, P2(0): 0, P3(0):0}

# Resolver el sistema de ecuaciones diferenciales con condiciones iniciales
soluciones = dsolve([eq1, eq2, eq3], ics=condiciones_iniciales)

# Mostrar las soluciones
print(soluciones)

#!Graficar las soluciones 
# Obtener las funciones solución
P1_solucion = soluciones[0].rhs
P2_solucion = soluciones[1].rhs
P3_solucion = soluciones[2].rhs

# Crear un rango de valores para t
t_valores = np.linspace(0, 1, 100)

# Evaluar las soluciones en el rango de valores de t
P1_valores = [P1_solucion.subs(t, valor) for valor in t_valores]
P2_valores = [P2_solucion.subs(t, valor) for valor in t_valores]
P3_valores = [P3_solucion.subs(t, valor) for valor in t_valores]

# Graficar las soluciones en un mismo gráfico
plt.plot(t_valores, P1_valores, label='P1(t)')
plt.plot(t_valores, P2_valores, label='P2(t)')
plt.plot(t_valores, P3_valores, label='P3(t)')

# Etiquetas y leyenda
plt.xlabel('Tiempo (t)')
plt.ylabel('Valores')
plt.legend()

# Mostrar la gráfica
plt.show()

# Graficar las soluciones en gráficos independientes
plt.figure(figsize=(12, 4))

# Graficar P1(t)
plt.subplot(131)
plt.plot(t_valores, P1_valores, label='P1(t)')
plt.xlabel('Tiempo (t)')
plt.ylabel('P1(t)')
plt.legend()

# Graficar P2(t)
plt.subplot(132)
plt.plot(t_valores, P2_valores, label='P2(t)')
plt.xlabel('Tiempo (t)')
plt.ylabel('P2(t)')
plt.legend()

# Graficar P3(t)
plt.subplot(133)
plt.plot(t_valores, P3_valores, label='P3(t)')
plt.xlabel('Tiempo (t)')
plt.ylabel('P3(t)')
plt.legend()

# Ajustar el diseño
plt.tight_layout()

# Mostrar los gráficos
plt.show()

#TODO  EJEMPLO 4.5==Para  un  transformador  de  distribución  se  ha  verificado  que  el  proceso  de  llegadas  de  las  fallas
#TODO  es  un  proceso  de  Poisson  homogéneo  (Proceso  de  renovación  exponencial)  con  una  tasa  de  ocurrencia 
#TODO  de  eventos   λ=0.2  fallas/año.
#! ====Cuál es el tiempo esperado para falla?========================
print(Funcion_exp(0.2))
#! Integrate describe the time to why for fail E(ttf)
Ti=0.2*t
#! En este caso se hizo una tabla con diferentes tiempos 
T_1=Ti.subs(t,1)
print("T_1=",T_1)
T_2=Ti.subs(t,5)
print("T_2=",T_2)
T_3=Ti.subs(t,10)
print("T_3=",T_3)
#!Probabilidad de llegada de fallas en diferentes periodos de tiempo:
def funcion_de_probabil_d_masa(k,t):#La probabilidad de que en un periodo dado t lleguen o ocurran exactamente k fallas está dada por:
    from sympy import factorial
    P_Nt_k=(1/(factorial(k)))*((0.2*t)**k)*exp(-0.2*t)
    return P_Nt_k

list_k=[0,1,2,3,4,5,6,7,8,9,10]
for i in list_k:
    falla_t_1=print("Analizando la probablidad de 1 a 10 fallas con t=1",funcion_de_probabil_d_masa(i,1))
    falla_t_5=print("Analizando la probablidad de 1 a 10 fallas con t=5",funcion_de_probabil_d_masa(i,5))
    falla_t_10=print("Analizando la probablidad de 1 a 10 fallas con t=10",funcion_de_probabil_d_masa(i,10))

#!Probabilidad de tener “al menos” una falla en diferentes periodos de tiempo:
for i in list_k:
    falla_t_1=print("Probablidaid de tener i fallas en t=1 ",1-(funcion_de_probabil_d_masa(i,1)))
    falla_t_5=print("Probablidaid de tener i fallas en t=5 ",1-(funcion_de_probabil_d_masa(i,5)))
    falla_t_10=print("Probablidaid de tener i fallas en t=10 ",1-(funcion_de_probabil_d_masa(i,10)))
    

#* -----Formulario de indice de confiabilidad estadistico ------

#T     Tiempo dr estudio o periodos de los registros ,generales[años]
#n     Número total de salidas en el periodo T
#nf    Número de fallas en el período T
#N     numero de componentes o longuitud total de o los componente(s)
#X     longuitud desconectada en una salida o falla dada
#Xpr   longuitud promedia desconectada en una salida o falla 
#tto   Tiempo para salida planeada,no planeada o falla 
#r     Tiempo medio para reaparación 
#MTTRS TIempo medio para restauración (reconexión de salidas planeadas y no planeadas)
# ttr  Tiempo de reparación 

def tasa_de_salida_(n,N,T,ttr,inicio,fin):# Aplica a uno o varios componentes no longitudinales 
    landa_0=n/(N*T-sum(range(inicio, fin + 1)))