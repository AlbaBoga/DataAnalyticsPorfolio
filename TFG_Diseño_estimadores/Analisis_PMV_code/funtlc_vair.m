function fval= funtlc_vair(x,vair,j,i)
load('datapmv');
hc2(1,i)=2.38.*(abs(x-ta(1,i)).^0.25);
hc1(1,j)=12.1.*sqrt(vair(1,j));
if hc1(1,j)>hc2(1,i)
    hc(1,j)=hc1(1,j);
else
    hc(1,j)=hc2(1,i);
end
fval= (tsk(1,i) - icl(1,i).*(3.96*0.00000001.*fcl(1,i).*((x+273)^4-(tr(1,i)+273).^4)+fcl(1,i).*hc(1,j).*(x-ta(1,i))))-x;

end