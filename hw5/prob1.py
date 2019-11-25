from numpy import matrix as mat
import numpy as np
from numpy.linalg import inv, eig, norm
from math import pi, atan, sqrt
from sys import exit


def h(vec):
    x = vec[0]
    y = vec[1]
    return atan(-y/(3-x))+atan((y+4)/(3-x))


def H(vec):
    x = vec[0,0]
    y = vec[1,0]
    xx3 = (3-x)**2
    yy = y**2
    yy4 = (y+4)**2

    temp = [-y/(xx3+yy) + (y+4)/(xx3+yy4), (x-3)/(xx3+yy) + (3-x)/(xx3+yy4)]

    return mat(temp)

def newt(x0,M0,V,z):
    x = x0
    M = M0
    
    while(True):
        hx = h(x)
        Hx = H(x)
        P = inv(inv(M)+(Hx.transpose()@mat(1/V)@Hx))
        gr = -(Hx.transpose()@mat(1/V)@mat(z-hx))
        print("gr: ",norm(gr))
        if norm(gr)<1E-6:
            break
        x = x- P@gr
    return x,P
z = 54.8 * pi/180



x0 = mat([[0],[0]])

M0 = mat([[0.2**2, 0], [0, 0.3**2]])

V = (0.4 * pi/180)**2

x,P = newt(x0,M0,V,z)
print("x:\n",x,"\nP:\n",P)

# error ellipse
vals, vecs = eig(P)

print("eigenvalues: ", vals, "\neigenvectors:\n", vecs, '\n')

print("direction: ",vecs[0,0]/vecs[1,0])
print(atan(vecs[0, 0]/vecs[1, 0]) * 180/pi)

print(sqrt(vals[0]/vals[1]))

print(", ".join(str(sqrt(num)) for num in vals))
