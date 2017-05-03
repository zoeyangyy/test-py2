from numpy import *
import matplotlib as plt

data = mat([[1, 2, 9, 8], [2, 3, 11, 14], [7, 9, 3, 2], [13, 15, 3, 1]])

u, sigma, vt = linalg.svd(data)

print "u=", u, "\nsigma=", sigma, "\nvt=", vt

sig = mat([[sigma[0], 0, 0], [0, sigma[1], 0], [0, 0, sigma[2]]])

print "result=", u[:, :3]*sig*vt[:3, :]

