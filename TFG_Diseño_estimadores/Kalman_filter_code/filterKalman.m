clear all;
load('trpie2013.mat');

Ts = 15;                            % Periodo de muestreo en minutos
sysD = c2d(tf(num,den),Ts);         % Pasamos a tiempo discreto
[numD denD] = tfdata(sysD,'v');     % Sacamos el numerador y denominador en tiempo discreto
[A, B, C, D]=tf2ss(numD,denD);      % Convertimos a modelo espacio - estados
sys = ss(A,[B B],C,D,Ts,'InputName',{'u' 'w'},'OutputName','y');  % Modelo dinámico de espacio-estados con un ruido de entrada w
 
Q = 2.3; 
R = 1;

[kalmf,L,~,Mx,Z] = kalman(sys,Q,R);
kalmf = kalmf(1,:);     % Descartamos la estimación de estados, solo nos interesa la primera salida que es nuestra salida a estimar

sys.InputName = {'u','w'};
sys.OutputName = {'yt'};
vIn = sumblk('y=yt+v');

kalmf.InputName = {'u','y'};
kalmf.OutputName = 'ye';

% Construimos el modelo de bloques
SimModel = connect(sys,vIn,kalmf,{'u','w','v'},{'yt','ye'});

t = (0:1:length(tair)-1)' * Ts;       % Vector de tiempo con un tiempo de muestreo dado por Ts
u = tair - tair(1);                   % Vector de entrada (hay que restarle el primer valor para situarlo en el punto de operación)
y = y2 - y2(1);                       % Vector de salida (hay que restarle el primer valor para situarlo en el punto de operación)

rng(10,'twister');                  % Semilla para el generador de números aleatorios
w = sqrt(Q)*randn(length(t),1);     % Ruido blanco de entrada
v = sqrt(R)*randn(length(t),1);     % Ruido blanco de salida

out = lsim(SimModel,[u,w,v]);       % Se simula el esquema construido

yt = out(:,1)+y2(1,1);      % Respuesta real
ye = out(:,2)+y2(1,1);      % Respuesta filtrada
y = yt + v;         % Respuesta medida por los sensores

% Diseño del filtro digital con una ventana de tamaño 10
windowSize = 10; 
b = (1/windowSize)*ones(1,windowSize);
a = 1;
y = filter(b,a,y);

% Se pintan los resultados obtenidos
clf
subplot(211), plot(t,y,'Color','#EDB120','LineStyle','-.');
hold on;
plot(t,yt,'b',t,ye,'r--'),
xlabel('Number of Samples'), ylabel('Output')
title('Kalman Filter Response')
legend('Sensor','True','Filtered')
subplot(212), plot(t,yt-y,'g',t,yt-ye,'r--'),
xlabel('Number of Samples'), ylabel('Error')
legend('True - measured','True - filtered')