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

figure
plot(z1,'b')
hold on
plot(z2,'r')
plot(x,'k')
legend("z1", "z2","x")
title("Two signals")
xlabel("Epochs")


batch = mean(z2);
seq = zeros(1000,1);
seq(1) = z2(1);
for n=2:epochs
    seq(n) = (n-1)/n * seq(n-1) + z2(n)/n;
end

figure
plot(seq,'k')
hold on
yline(batch,'--k');
plot(x,':k')
legend("sequential", " batch","true")
title("two averaging filters")