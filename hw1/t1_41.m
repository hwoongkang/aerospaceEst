clear; close all;

p = 0.001;
N = 5000;

% bernouille wrapper
myFun = @(m) bernouille(N,p,m);

% cumulative probability
cumul = 0;

m = -1;
% halt when the prob. becomes 0.98
while (cumul<=0.98)
    m = m+1;
    cumul = cumul + myFun(m);
end

fprintf("P = 0.98 at m = %d\n",m);

%% over/underflow - safe bernouille
function f = bernouille(N,p,m)
    %f = nchoosek(N,m) * p^m * (1-p) ^ (N-m);
    % mySum: sum of log
    function out = mySum(n)
        out = 0;
        for count = 1:n
            out = out + log(count);
        end
    end
    % overflow-safe nCk using log sum
    log_nCm = mySum(N) - mySum(N-m) - mySum(m);
    
    % underflow - safe bernouille using log
    logF = log_nCm + m*log(p) + (N-m) * log(1-p);
    
    % return the exponentiated value
    f = exp(logF);
end
