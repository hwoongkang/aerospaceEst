clear; close all;

% N(5,2^2)
numSample = 10000;
x = 2* randn(1,numSample) + 5;
% plot
figure;
plot(x,'k')
xlabel("samples")
title("N(5,2^2)")

% print mean, std and plot
figure
% get counts
[counts,xvalues] = hist(x,-3:1:13);
% plot relative freq.
bar(xvalues,counts/numSample)
fprintf("mean: %.4f, std: %.4f\n",mean(x),std(x,1));
hold on
ax = gca;
xx = linspace(ax.XLim(1), ax.XLim(2),1000);
plot(xx,normpdf(xx,5,2),'--k','LineWidth',1)
legend("Sampled", "Theoritical")
title("N(5,2^2)")