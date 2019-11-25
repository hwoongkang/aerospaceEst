import numpy as np
from numpy.random import normal as rand
import matplotlib.pyplot as plt

x0 = 0

alphas = [0.5,1.5]

initialUncertainties = [100,1,0.01]

W = 0.2**2
V = 0.2**2

w = 0.2
v = 0.2


for alpha in alphas:
    for X0 in initialUncertainties:
        xPrior = [np.sqrt(X0)*rand()]
        xPost = []
        M = [X0]
        P = []
        K = []
        for epoch in range(100):
            pTemp = 1/(1/M[-1] + 1/V)
            P.append(pTemp)
            kTemp = pTemp/V
            K.append(kTemp)

            M.append(pTemp + W)

            z = xPrior[-1] + v*rand()

            xPost.append(xPrior[-1]+kTemp*(z - xPrior[-1]))

            xPrior.append(alpha * xPost[-1] + w*rand())
        
        npX = np.array(xPost)
        npP = np.array(P)

        xPlus = npX + np.sqrt(npP)
        xMinus = npX - np.sqrt(npP)

        plt.figure()
        plt.plot(npX,'k')
        plt.plot(xMinus,'--r')
        plt.plot(xPlus,'--r')
        plt.title(r'$\alpha = $'+str(alpha)+r', $X_0 = $'+str(X0))
        plt.savefig("./figures/p1_alpha_"+str(alpha)+"_X0_"+str(X0)+".jpg")

