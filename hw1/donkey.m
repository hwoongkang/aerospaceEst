close all;

r = 1E7;
x = 0.5;

myAns = reduceTo(x,r);

plotX = linspace(0,myAns+1,1000);
figure;

plot(plotX, water(r,plotX),'k');

%% first function
function V = water(r,t)
    V = 1E9 + 1E8 * (1 - exp(-t/100)) - r*t;
end

%% reduce to 50%

function days = reduceTo(x,r)
    % 0 < x < 1
    
    myFun = @(n) water(r,n) - 1E9*x;
    
    fprintf("zero: %.3f\n", fzero(myFun,0));
    
    days = fzero(myFun,0);
    
end

