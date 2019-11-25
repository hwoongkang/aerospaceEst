from numpy import matrix as mat
from numpy.linalg import inv,eig
from math import pi, atan, sqrt

# measurement
H = mat([4/25, -1/3 + 3/25])

# meas noise
V = (0.4 * pi / 180) ** 2

# a priori uncertainty
M = mat([[0.2**2,0],[0,0.3**2]])

# a posteriori uncertainty
C = inv(M) + H.transpose()@(mat(1/V))@H

# innovation? vector?
b = -(54.8 * pi/180 - atan(4/3)) * 1/V * H

print("b: ",b)

x_new = -inv(C)@b.transpose()
print("x_new: ", x_new, '\n')

P = inv(C)
print("P: ", P,'\n')

# error ellipse
vals, vecs = eig(P)

print("eigenvalues: ", vals, "\neigenvectors:\n",vecs,'\n')

print(atan(vecs[0,0]/vecs[1,0]) * 180/pi)

print(sqrt(vals[0]/vals[1]))

print(", ".join(str(sqrt(num)) for num in vals))