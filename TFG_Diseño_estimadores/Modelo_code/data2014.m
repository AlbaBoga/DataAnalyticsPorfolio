clear all
clc
mat = dir('*.mat');
file={};
for n = 1:length(mat)
    load(mat(n).name);
    if mat(n).bytes>4433%elimina los que están vacíos
    file{n,1}=zeros(length(data.data),width(data.data));
    file{n,1}=data.data;
    end
end
A=cell2mat(file);

sensor1=A(:,2);%pared sur ºC
sensor1(sensor1<0)=[];
% sensor1(sensor1<15)=[];
sensor2=A(:,3);%pared este ºC
sensor2(sensor2<0)=[];
% sensor2(sensor2<15)=[];
sensor3=A(:,4);%pared norte ºC
sensor3(sensor3<0)=[];
% sensor3(sensor3<15)=[];
sensor4=A(:,5);%pared oeste ºC
sensor4(sensor4<0)=[];
% sensor4(sensor4<15)=[];
sensor5=A(:,6);%suelo ºC
sensor5(sensor5<0)=[];
% sensor5(sensor5<15)=[];
sensor6=A(:,7);%techo ºC
sensor6(sensor6<0)=[];
% sensor6(sensor6<15)=[];
tair=A(:,8);% temp aire ºC
tair(tair<0)=[];
tair(tair<10)=[];

ase=min(length(sensor1),length(sensor2));
bse=min(length(sensor3),length(sensor4));
cse=min(length(sensor5),length(sensor6));
dse=min(ase,bse);

%Escoge la longitud del vector menor para que tengan 
%el mismo tamaño
%Después calcúla la temperatura radiante media para 
%una persona sentada y de pie
for i=1:1:min(cse,dse)
   sensor1(i,1);
   sensor2(i,1);
   sensor3(i,1);
   sensor4(i,1);
   sensor5(i,1);
   sensor6(i,1);
   trsentado(i,1)=((0.1*(sensor5(i,1)+sensor6(i,1)))+(0.22*(sensor2(i,1)+sensor4(i,1)))+(0.3*(sensor3(i,1)+sensor1(i,1))))/(2*(0.18+0.22+0.3));
   trpie(i,1)=((0.08*(sensor5(i,1)+sensor6(i,1)))+(0.23*(sensor2(i,1)+sensor4(i,1)))+(0.35*(sensor3(i,1)+sensor1(i,1))))/(2*(0.08+0.23+0.35));
end
%Elimino los picos para que quede dentro de un rango
trsentado(trsentado<0)=[];
trsentado(trsentado<10)=[];
trpie(trpie<0)=[];
trpie(trpie<10)=[];

%tiempos
t = (1:1:length(tair))';
t1 = (1:1:length(trpie))';
t2 = (1:1:length(trsentado))';

for i=1:1:length(tair)
    tair_tf(i,1)=tair(i,1)-tair(1,1);
end

%trsentado
G=tf(0.005458,[1 0.006033]); %función obtenida ident
u1 = tair_tf;
y1 = lsim(G,u1,t)+trsentado(1,1);

%trpie
G=tf(0.004859,[1 0.004747]); %función obtenida ident
u2 = tair_tf;
y2 = lsim(G,u2,t)+trpie(1,1);


figure(1) %tair y trpie
title('Tair/Tr levantado')
hold on
plot(t,tair,'b');
plot(t1,trpie,'r');
grid;
xlabel('Tiempo [s]')
ylabel('Temperatura [ºC]')
legend({'Temperatura del aire','Temperatura radiante media, levantado'}, 'FontSize',17)

figure(2) % tair y trsentado
hold on
plot(t,tair,'b');
plot(t2,trsentado,'r');
grid;
title('Tair/Tr sentado')
xlabel('Tiempo [s]')
ylabel('Temperatura [ºC]')
legend({'Temperatura del aire','Temperatura radiante media, sentado'}, 'FontSize',17)

figure(3) %tras hacer el for con desfase veo que mi nuevo
hold on %trsentado y el trsentado de la formula coinciden
plot(t,y1,'b');
plot(t2,trsentado,'r');
grid;
title('Tr sentado')
xlabel('Tiempo [s]')
ylabel('Temperatura [ºC]')
legend({'tr, sentado, funcion transferencia','tr, sentado, sensores'}, 'FontSize',17)

figure(4) %tras hacer el for con desfase veo que mi nuevo
hold on %trpie y el trpie de la formula coinciden
plot(t,y2,'b');
hold on
plot(t1,trpie,'r');
grid;
title('Tr levantado')
xlabel('Tiempo [s]')
ylabel('Temperatura [ºC]')
legend({'tr, levantado, funcion transferencia','tr, levantado, sensores'}, 'FontSize',17)

