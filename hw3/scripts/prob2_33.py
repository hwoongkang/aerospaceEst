import numpy as np
import matplotlib.pyplot as plt


def generateGaussMarkov(sigma, beta, delT):
    x0 = np.random.normal(0, sigma)
    sigmaWhite = np.sqrt(sigma*sigma * (1-np.exp(-2*beta*delT)))
    
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

np.random.seed(0)
sigma = 1
beta = 1
delT = 0.05

mySeq = generateGaussMarkov(sigma, beta, delT)

lags = np.array([i for i in range(61)])

autocorr = np.array([computeAutoCorr(mySeq,lag) for lag in lags])

myExp = lambda x: sigma**2 * np.exp(-beta * abs(x))
theory = np.array([myExp(lag*delT) for lag in lags])

plt.figure()

plt.plot(lags*delT,autocorr, 'k',label = "experimental")
plt.plot(lags*delT,theory,'r', label = "theoritical")
plt.legend()
plt.title("Autocorrelation")
plt.xlabel("time lag [s]")

plt.savefig("./figures/gaussMarkov.jpg")
