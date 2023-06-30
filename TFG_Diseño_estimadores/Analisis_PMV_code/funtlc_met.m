function fval= funtlc_met(x,vair,i,j)
load('datapmv');
hc2(1,i)=2.38.*(abs(x-ta(1,i)).^0.25);
hc1(1,i)=12.1.*sqrt(vair(1,i));
if hc1(1,i)>hc2(1,i)
    hc(1,i)=hc1(1,i);
else
    hc(1,i)=hc2(1,i);
end
fval= (tsk(1,j) - icl(1,i).*(3.96*0.00000001*fcl(1,i).*((x+273)^4-(tr(1,i)+273).^4)+fcl(1,i).*hc(1,i).*(x-ta(1,i))))-x;

end