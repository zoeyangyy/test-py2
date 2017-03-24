from numpy import *

data = mat([[1, 2, 3], [2, 3, 4], [5, 7, 8], [2, 5, 9]])

u, sigma, vt = linalg.svd(data)

print "u=", u, "\nsigma=", sigma, "\nvt=", vt

sig = mat([[sigma[0], 0, 0], [0, sigma[1], 0], [0, 0, sigma[2]]])

print "result=", u[:, :3]*sig*vt[:3, :]
