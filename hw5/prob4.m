t = pi/3;

V = 0.5;

c = @cos;
s = @sin;

A = [c(t), s(t); -s(t), c(t)];

G = eye(2);

C = [1, 0];

Q11 = (2*t - s(2*t))/4;
Q12 = (1-c(2*t))/4;
Q22 = (2*t + s(2*t))/4;

Q = [Q11, Q12;Q12, Q22];

R = V;

format short 

[K,M,P] = dlqe(A,G,C,Q,R)