A = [1, 1; 0, 1];
G = eye(2);
C = [1, 0];
Q = [1/3, 1/2; 1/2, 1];
R = 2;

format short 

[K,M,P] = dlqe(A,G,C,Q,R)