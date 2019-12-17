Ts = 0.4;

ch = @cosh;
sh = @sinh;

A = [ch(Ts), sh(Ts); sh(Ts), ch(Ts)];
B = [ch(Ts) - 1; sh(Ts)];
Q = 0;
R = Ts;
N = 0;

[K,S,e] = dlqr(A,B,Q,R,N)