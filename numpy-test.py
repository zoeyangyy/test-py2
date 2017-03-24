# coding:utf-8

import numpy as np

# w = np.random.randn(10, 5) * 0.001

x1 = np.array([1, 2, 3, 4])
x2 = np.array([5,6,7,8])

x = np.matrix([[1,2,3,4],[5,6,7,8]]).T
y = np.array([1,2])

W = np.random.rand(3, 4) * 0.1
print W


def L_i(x, y, W):
    # unvectorized version
    delta = 1.0
    scores = W.dot(x)
    correct_class_score = scores[y]
    D = W.shape[0]  # 有多少行
    loss_i = 0.0
    for j in xrange(D):
        if j == y:
            continue
        loss_i += max(0, scores[j] - correct_class_score + delta)
    return loss_i


def L_i_vectorized(x, y, W):
    delta = 1.0
    scores = W.dot(x)
    margins = np.maximum(0, scores - scores[y] + delta)
    # print(np.maximum(0, scores))
    # print np.maximum(0, scores - scores[y])
    margins[y] = 0
    loss_i = np.sum(margins)
    return loss_i


def L(x, y, W):
    delta = 1.0
    scores = W.dot(x).T
    loss_i = 0.0
    for j in range(scores.shape[0]):
        margins = np.maximum(0, scores[j] - scores[j, y[j]] + delta)
        margins[0, y[j]] = 0
        loss_i += np.sum(margins)
    return loss_i / scores.shape[0]


print (L_i(x1, 1, W) + L_i(x2, 2, W))/2
print L(x, y, W)


def eval_numerical_gradient(f, x):
    fx = f(x)
    grad = np.zeros(x.shape)
    h = 0.001

    it = np.nditer(x, flags=['multi_index'],op_flags=['readwrite'])
    while not it.finished:

        ix = it.multi_index
        old_value = x[ix]
        x[ix] = old_value + h
        fxh = f(x)
        x[ix] = old_value

        grad[ix] = (fxh - fx) / h
        it.iternext()

    return grad


def CIFAR10_loss_fun(W):
    return L(x, y, W)


origin = 0
while abs(L(x, y, W) - origin) > 0.01:
    origin = L(x, y, W)
    df = eval_numerical_gradient(CIFAR10_loss_fun, W)
    W -= 0.01 * df

print origin
