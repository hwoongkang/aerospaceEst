T = 0.4;

c = @cosh;
s = @sinh;

A = [c(T), s(T); s(T), c(T)];
G = eye(2);
C = [0, 1];
Q = 8/4 * [s(2*T) - 2*T, c(2*T)-1; c(2*T)-1, s(2*T) + 2*T];
R = 1;
tic
[M,P,Z,E] = dlqe(A,G,C,Q,R);
toc

figure
hold on
for ratio = 0:.1:10
    Q = ratio/4 * [s(2*T) - 2*T, c(2*T)-1; c(2*T)-1, s(2*T) + 2*T];
    [~,~,~,E] = dlqe(A,G,C,Q,R);
    if ratio== 0
        E
    end
    for dim=1:2
        rea = real(E(dim));
        img = imag(E(dim));
        plot([rea,-rea],[img,img],'.k');
        drawnow
    end
end