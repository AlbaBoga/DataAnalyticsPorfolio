function fval= funtlc_ta(x,vair,j,i)
load('datapmv');
HcA(1,i) = 12.1.*sqrt(vair(1,i));
HcB(1,j) = 2.38 * abs(tclini(1,j) - ta(1,j)) .^ 0.25;
if(HcA(1,i) > HcB(1,j))
    hc(1,j) = HcA(1,i);
else
    hc(1,j) = HcB(1,j);
end
fval= (tsk(1,i) - icl(1,i).*(3.96*0.00000001.*fcl(1,i)*((x+273)^4-(tr(1,i)+273).^4)+fcl(1,i).*hc(1,j).*(x-ta(1,j))))-x;

end