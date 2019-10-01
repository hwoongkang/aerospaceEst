cmin = 6.8;
cmax = 9.2;
fun = @(x) -x^2 * (30 - 2.5 *x)^2 / (x^2 + (30-2.5*x)^2);

[x,val] = fminbnd(fun,cmin,cmax)