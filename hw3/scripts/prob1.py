import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def f1(x):
    if (abs(x)<0.5):
        return 1
    else:
        return 0

def f2(x):
    if (abs(x)>1):
        return 0
    elif (x<0):
        return 1+x
    else:
        return 1-x

def f3(x):
    if (x < -1.5):
        return 0
    elif (x < -0.5):
        return (x*x + 3*x + 9/4)/2
    elif (x < 0.5):
        return (3/4 - x*x)
    elif (x < 1.5):
        return (x*x - 3*x + 9/4)/2
    else:
        return 0


x = np.linspace(-3, 3, 1000)

myNorm = (lambda x,mu: norm.pdf(x,0,mu))

y1 = np.array([f1(xx) for xx in x])
z1 = np.array([myNorm(xx,np.sqrt(1/12)) for xx in x])

y2 = np.array([f2(xx) for xx in x])
z2 = np.array([myNorm(xx,np.sqrt(1/6)) for xx in x])

y3 = np.array([f3(xx) for xx in x])
z3 = np.array([myNorm(xx,np.sqrt(1/4)) for xx in x])


plt.figure()
ax1 = plt.subplot(311,title="P1")
f1 = ax1.plot(x, y1, 'k', label = "P")
f2 = ax1.plot(x, z1, 'r', label = "Normal")
ax1.legend()
ax2 = plt.subplot(312,title="P2")
ax2.plot(x, y2, 'k')
ax2.plot(x, z2, 'r')
ax3 = plt.subplot(313,title="P3")
ax3.plot(x, y3, 'k')
ax3.plot(x, z3, 'r')

plt.tight_layout()

plt.savefig("./figures/prob1c.jpg")
