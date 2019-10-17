import numpy as np
import matplotlib.pyplot as plt


def approxNormal(k):
    w = 0
    for _ in range(k):
        w += np.random.uniform(0, 1)
    return w-(k//2)


np.random.seed(0)

N = 1000
approxed = np.array([approxNormal(12) for _ in range(N)])

bins = np.arange(-3.9, 3.9, 0.3)


count, bins = np.histogram(approxed, bins)

plt.figure()
plt.hist(approxed, bins)

x = np.linspace(-4,4,1000)
y = 300 * np.exp(-x*x/2)/(np.sqrt(2*np.pi))

plt.plot(x, y)

plt.savefig("./figures/histogram.jpg")
