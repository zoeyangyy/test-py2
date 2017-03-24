# ！python2
# -*- coding: utf-8 -*-

x_old = 0
x_new = 2
eps = 0.01  # step size
precision = 0.00001


def f_derivative(x):
    return 4 * x**3 - 9 * x**2

while abs(x_new-x_old) > precision:
    x_old = x_new
    x_new = x_old - eps * f_derivative(x_old)

print "local minimum occurs at ", x_new

# f(x) = x^4 - 3x^3 + 2, 结果得到极小值或者鞍值
