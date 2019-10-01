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

z1 = 4+v1;
z2 = 4+v2;

figure
plot(z1,'b')
hold on
plot(z2,'r')
legend("z1", "z2")
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
legend("sequential", " batch")
title("two averaging filters")

batchSig = sig2/sqrt(epochs);
t = 1:epochs;
seqSig = sig2./sqrt(t);

figure
plot(seqSig,'k')
hold on
yline(batchSig,'--k'); grid on
legend("Sequential","batch")
title("Std of two averaging filters")