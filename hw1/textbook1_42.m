chi1 = @(x) chiWithN(1,x);
chi2 = @(x) chiWithN(2,x);
chi4 = @(x) chiWithN(4,x);
x = linspace(0,10);

figure;
one = plot(x,chi1(x),'k');
hold on;
two = plot(x,chi2(x),'--k');
hold on;
four = plot(x,chi4(x),'-.k');
legend([one,two,four],["n=1","n=2","n=4"]);

title("Chi Square Distribution");

figure;
mu = 16;
x = linspace(0,2*mu,50*mu);
chichi = plot(x,chiWithN(mu,x),'k');
hold on
gau = plot(x,normpdf(x,mu,sqrt(2*mu)),'--k');

legend([chichi,gau],[sprintf("Chi sqaure with n=%d",mu),sprintf("N(%d,%d)",mu,2*mu)])

function y = chiWithN(n,x)
    if x<=0
        y = 0;
    else
        y = ((x.^(n/2 -1)) .* exp(-x/2)) ./ ( 2^(n/2) ) ./ gamma(n/2) ;
    end
end