fun = @(x) -x(1) -x(2);
nonlin = @myFun;
[x,val] = fmincon(fun,[0.4;1.6],[],[],[],[],[],[],nonlin)


function [c,out] = myFun(x)
    temp1 = (10 - 2*x(1))^2;
    temp2 = (15 - 5*x(2))^2;
    out = temp1*temp2 / (temp1+temp2) - 6^2;
    c = [];
end