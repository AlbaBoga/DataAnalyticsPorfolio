clear all
clc

% M 46 w/m2 to 232 W/m2 (0.8 met to 4 met)
% Icl 0 m2K/W to 0.310 m2k/W (0clo to 2 clo)
% ta 10ºC to 30ºC
% tr 10ªC to 40ªC
% var 0 m/s to 1 m/s
% pa 0Pa to 2700 Pa
% W=0??
%tcl 31.6ºC to 33.5ºC
% Datos tomados de ISO 7730:2005(E)
ta=10:1:40; %rango temp aire
met=[0.8,1.6,2.4,3.2,4]; %rango actividad metabólica
clo=[0.000000000001,0.5,1,1.5,2]; %rango aislamiento de la ropa
tr=[10,17.5,25,32.5,40]; %rango temp radiante media
vair=[0.000000000001,0.25,0.5,0.75,1];%rango velocidad del aire
rh=[30,40,50,60,70]; %rango humedad relativa
pmv_a=zeros(5,31); %vector pmv vacío

for j=1:1:31
    for i=1:1:5
met(1,i);
clo(1,i);
m(1,i)=met(1,i).*58.15; %W/m2      -- M
icl(1,i)=clo(1,i).*0.155;%m2ºC/w  -- RCL
ta(1,j); %ºc
tak(1,j)=ta(1,j)+273;
tr(1,i); %ºc
vair(1,i); %m/s
rh(1,i);%porcentaje
%cálculo presión parcial vápor de agua
c8=-5.8002206*1000;
c9=1.3914993;
c10=-4.8640239*0.01;
c11=4.1764768*0.00001;
c12=-1.4452093*0.00000001;
c13=6.5459673;
lnpws(1,j)=(c8./tak(1,j))+(c9)+(c10.*tak(1,j))+(c11*tak(1,j).^2)+(c12*tak(1,j).^3)+(c13.*log(tak(1,j)));
pws(1,j)=exp(lnpws(1,j));
pa(1,j)=(rh(1,i).*pws(1,j))/100; 

w=0; %effective mechanical power
tclini(1,j)=ta(1,j); %supongo que el valor inicial de la temperatura de la ropa
                     % es igual a la temperatura del aire
tsk(1,i)=35.7-(0.028.*(m(1,i)-w));
fcl1(1,i)=1+(0.2.*clo(1,i));
fcl2(1,i)=1.05+(0.1.*clo(1,i));
%Calculo el factor del area de superficie de la ropa
if clo(1,i)<=0.5 
    fcl(1,i)=fcl1(1,i);
else
    fcl(1,i)=fcl2(1,i);
end
%calculo el coeficiente de transferencia de calor convectivo
HcA(1,i) = 12.1.*sqrt(vair(1,i));
HcB(1,j) = 2.38 * abs(tclini(1,j) - ta(1,j)) .^ 0.25;
if(HcA(1,i) > HcB(1,j))
    hc(1,j) = HcA(1,i);
else
    hc(1,j) = HcB(1,j);
end

%estimo la temperatura superficial de la ropa
save('datapmv');
options = optimset('Display','off','Algorithm','levenberg-marquardt');
tcl(1,j)=fsolve(@funtlc_ta,tclini(1,j),options,vair(1,i),j,i);

%Cálculo PMV
pmv1=0.303.*exp(-0.036*m(1,i))+0.028; %thermal sensation 
pmv2(1,j)=3.05*0.001.*(5733-6.99.*(m(1,i)-w)-pa(1,j));%heat loss diff through skin
pmv3=0.42.*(m(1,i)-w-58.15);%heat loss by sweating
pmv4(1,j)=1.72*0.00001.*m(1,i).*(5867-pa(1,j));%latent respiration heat loss
pmv5(1,j)=0.0014.*m(1,i).*(34-ta(1,j));%dry respiration heat loss
pmv6(1,j)=3.96*0.00000001.*fcl(1,i).*(((tcl(1,j)+273)).^4-((tr(1,i)+273)).^4);%heat loss by radiation
pmv7(1,j)=fcl(1,i)*hc(1,j).*(tcl(1,j)-ta(1,j));%heat loss by convection

pmv(1,j)=pmv1.*((m(1,i)-w)-pmv2(1,j)-pmv3-pmv4(1,j)-pmv5(1,j)-pmv6(1,j)-pmv7(1,j));

pmv_a(i,j)=pmv(1,j);
    end
end
%Gráfica
plot(ta,pmv_a(1,:));
  grid;
  hold on;
  plot(ta,pmv_a(2,:));
  hold on;
  plot(ta,pmv_a(3,:));
  hold on;
  plot(ta,pmv_a(4,:));
  hold on;
  plot(ta,pmv_a(5,:))
  title('Temperatura del aire/PMV')
    xlabel('ºC')
    ylabel('PMV')
    legend('Valor mínimo', 'Segundo valor', 'Valor medio', 'Cuarto valor', 'Valor máximo')