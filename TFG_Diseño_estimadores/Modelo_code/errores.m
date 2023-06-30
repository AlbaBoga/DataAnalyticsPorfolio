% Error entre los datos reales y los estimados
clear all;
clc;
load('resultados2013')

% Datos reales.
Real_1= trsentado_new;
max_Real_1 = max(Real_1)
min_Real_1 = min(Real_1)
Real_2 = trpie_new;
max_Real_2 = max(Real_2)
min_Real_2 = min(Real_2)

% Datos estimados.
Estimado_1 = y1;
max_Estimado_1 = max(Estimado_1)
min_Estimado_1 = min(Estimado_1)
Estimado_2 = y2; 
max_Estimado_2 = max(Estimado_2)
min_Estimado_2 = min(Estimado_2)

%Cálculo del error absoluto.
%Para la temperatura radiante media cuando la persona está sentada.
e1=Real_1-Estimado_1;
abs_e1=abs(e1);
max_e1=max(abs_e1)
min_e1=min(abs_e1)
%Para la temp radiante media cuando la persona está de pie.
e2=Real_2-Estimado_2;
abs_e2=abs(e2);
max_e2=max(abs_e2)
min_e2=min(abs_e2)
% Cálculo de la media del error absoluto.
%Persona sentada
mean_abs_e1=mean(abs_e1)
%Persona levantada
mean_abs_e2=mean(abs_e2)

%Cálculo del error relativo
%Persona sentada
r1 = abs_e1./abs(Real_1);
max_r1=max(r1)
min_r1=min(r1)
%Persona levantada
r2 = abs_e2./abs(Real_2);
max_r2=max(r2)
min_r2=min(r2)
%Cálculo de la media del error relativo
%Persona sentada
mean_r1=mean(r1)
%Persona levantada
mean_r2=mean(r2)