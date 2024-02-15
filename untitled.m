syms t Ps T D m r P0(t) P1(t) P2(t) P3(t)

% Definir el sistema de ecuaciones diferenciales
eq1 = diff(P0) == -(((1 - Ps) / T) + (Ps / T)) * P0 + (1 / T) * P1 + (1 / r) * P3;
eq2 = diff(P1) == -((1 / D) + (1 / r)) * P1 + ((1 - Ps) / T) * P0 + (1 / m) * P2;
eq3 = diff(P2) == -((1 / m) + (1 / D)) * P2 + (Ps / T) * P0 + (1 / r) * P1 + (1 / T) * P3;
eq4 = diff(P3) == -((1 / r) + (1 / T)) * P3 + ((1 / D) * P2);

% Especificar condiciones iniciales en t = 0
condiciones_iniciales = [P0(0) == 0, P1(0) == 1, P2(0) == 0, P3(0) == 0,P0(t)+P1(t)+P2(t)+P3(t)==1];

% Resolver el sistema de ecuaciones diferenciales con condiciones iniciales
soluciones = dsolve([eq1, eq2, eq3, eq4], condiciones_iniciales);
disp(soluciones)
