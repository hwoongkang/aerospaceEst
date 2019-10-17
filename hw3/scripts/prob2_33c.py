import numpy as np
import matplotlib.pyplot as plt


def generateGaussMarkov(sigma, beta, delT):
    x0 = np.random.normal(0, sigma)
    sigmaWhite = np.sqrt(sigma*sigma * (1-np.exp(-2*beta*delT)))
    #sigmaWhite =1
    mySeq = [x0]

    for _ in range(1023):
        mySeq.append(mySeq[-1] * np.exp(-beta*delT) +
                     np.random.normal(0, sigmaWhite))
    return np.array(mySeq)

def computeAutoCorr(signal,lag):
    N = len(signal)
    if lag>=N:
        return 0   
    out = 0
    for i in range(N-lag):
        out += signal[i] * signal[i+lag]
    return out/N

np.random.seed(10)
sigma = 1
beta = 1
delT = 0.05

lags = np.array([i for i in range(61)])


myExp = lambda x: sigma**2 * np.exp(-beta * abs(x))
theory = np.array([myExp(lag*delT) for lag in lags])

x = lags * delT

plt.figure()

plt.plot(x, theory, 'k', label = "theory")

sumCorr = np.zeros(len(lags))
print(sumCorr)
for i in range(1,9):
    mySeq = generateGaussMarkov(sigma, beta, delT)
    autocorr = np.array([computeAutoCorr(mySeq,lag) for lag in lags])
    
    sumCorr += autocorr
    
    if i == 1:
        one_ = sumCorr.copy()
    elif i ==2:
        two = sumCorr.copy()/2
    elif i ==4:
        four = sumCorr.copy()/4
    elif i ==8:
        eight = sumCorr.copy()/8

print(x)
plt.plot(x,one_,label = "one_")
plt.plot(x,two,label = "two")
plt.plot(x,four,label = "four")
plt.plot(x,eight, label = "eight")
    
plt.legend()

plt.savefig("./figures/converging.jpg")
