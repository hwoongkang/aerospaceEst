close all; clear;

epochs = 1000;
sig1 = 2;
sig2 = 3;
v1 = sig1 * randn(epochs,1);
v2 = sig2 * randn(epochs,1);

figure
plot(v1,'k')
hold on
plot(v2+20,'--k')
legend("v1", "v2 + 20")
title("Two noises")
xlabel("Epochs")

t = (1:epochs).';
x = sin(2*pi*t/500);
z1 = x+v1;
z2 = x+v2;

hat = zeros(1000,1);

Ns = [4,9,25,100,400];


titles = strings(1,6);
figure;
plot(x,'k')
titles(1) = "true";
hold on;
for ind = 1:length(Ns)
    N = Ns(ind);
    hat = hat * 0;
    hat(1) = z2(1);
    for k = 2:epochs
        hat(k) = (N-1) / N * hat(k-1) + z2(k) /N;
    end
    plot(hat);
    titles(ind+1) = sprintf("N=%d",N);
end
legend(titles)
xlabel("samples")
title("Moving averaging filters")