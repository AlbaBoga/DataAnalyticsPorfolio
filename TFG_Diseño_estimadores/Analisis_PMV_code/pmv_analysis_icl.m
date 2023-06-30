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
clo=0.000000000001:0.060606:2; %rango aislamiento de la ropa
met=[0.8,1.6,2.4,3.2,4]; %rango actividad metabólica
ta=[10,17.5,25,32.5,40]; %rango temp aire
tr=[10,17.5,25,32.5,40]; %rango temp radiante media
vair=[0.000000000001,0.25,0.5,0.75,1]; %rango velocidad del aire
rh=[30,40,50,60,70]; %rango humedad relativa
pmv_a=zeros(5,34);%vector pmv vacío

for j=1:1:34
    for i=1:1:5
clo(1,j);
met(1,i);
m(1,i)=met(1,i).*58.15; %W/m2      -- M
icl(1,j)=clo(1,j).*0.155;%m2ºC/w  -- RCL
ta(1,i); %ºc
tak(1,i)=ta(1,i)+273;
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
lnpws(1,i)=(c8./tak(1,i))+(c9)+(c10.*tak(1,i))+(c11.*tak(1,i).^2)+(c12.*tak(1,i).^3)+(c13.*log(tak(1,i)));
pws(1,i)=exp(lnpws(1,i));
pa(1,i)=(rh(1,i).*pws(1,i))./100; 

w=0; %effective mechanical power
tclini(1,i)=ta(1,i); %supongo que el valor inicial de la temperatura de la ropa
                     % es igual a la temperatura del aire
tsk(1,i)=35.7-(0.028.*(m(1,i)-w));
fcl1(1,j)=1+(0.2.*clo(1,j));
fcl2(1,j)=1.05+(0.1.*clo(1,j));
%Calculo el factor del area de superficie de la ropa
if clo(1,j)<=0.5 
    fcl(1,j)=fcl1(1,j);
else
    fcl(1,j)=fcl2(1,j);
end
%calculo el coeficiente de transferencia de calor convectivo
HcA(1,i) = 12.1.*sqrt(vair(1,i));
HcB(1,i) = 2.38 .* abs(tclini(1,i) - ta(1,i)) .^ 0.25;
if(HcA(1,i) > HcB(1,i))
    hc(1,i) = HcA(1,i);
else
    hc(1,i) = HcB(1,i);
end

%estimo la temperatura superficial de la ropa
save('datapmv');
options = optimset('Display','off','Algorithm','levenberg-marquardt');
tcl(1,j)=fsolve(@funtlc_clo,tclini(1,i),options,vair(1,i),j,i);

%Cálculo PMV
pmv1=0.303*exp(-0.036.*m(1,i))+0.028; %thermal sensation 
pmv2=3.05*0.001*(5733-6.99.*(m(1,i)-w)-pa(1,i));%heat loss diff through skin
pmv3=0.42.*(m(1,i)-w-58.15);%heat loss by sweating
pmv4=1.72*0.00001.*m(1,i).*(5867-pa(1,i));%latent respiration heat loss
pmv5=0.0014.*m(1,i).*(34-ta(1,i));%dry respiration heat loss
pmv6(1,j)=3.96*0.00000001.*fcl(1,j).*(((tcl(1,j)+273)).^4-((tr(1,i)+273)).^4);%heat loss by radiation
pmv7(1,j)=fcl(1,j).*hc(1,i).*(tcl(1,j)-ta(1,i));%heat loss by convection

pmv(1,j)=pmv1.*((m(1,i)-w)-pmv2-pmv3-pmv4-pmv5-pmv6(1,j)-pmv7(1,j));

pmv_a(i,j)=pmv(1,j);
    end
end
%Gráfica
  plot(clo,pmv_a(1,:));
  grid;
  hold on;
  plot(clo,pmv_a(2,:));
  hold on;
  plot(clo,pmv_a(3,:));
  hold on;
  plot(clo,pmv_a(4,:));
  hold on;
  plot(clo,pmv_a(5,:))
  title('Aislamiento de la ropa/PMV')
    xlabel('clo')
    ylabel('PMV')
    legend('Valor mínimo', 'Segundo valor', 'Valor medio', 'Cuarto valor', 'Valor máximo')