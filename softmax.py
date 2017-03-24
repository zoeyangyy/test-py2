# -*- coding: utf-8 -*-

import numpy as np

def softmax(x):

    """Compute softmax values for each sets of scores in x."""
    pass # TODO: Compute and return softmax(x)
    x = np.array(x)
    x = np.exp(x)
    x.astype('float32')
    if x.ndim == 1:
        sumcol = sum(x)
        for i in range(x.size):
            x[i] /= float(sumcol)

    if x.ndim > 1:
        sumcol = x.sum(axis=0)
        for row in x:
            for i in range(row.size):
                row[i] /= float(sumcol[i])
    return x


def softmax2(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)

# 测试结果
scores = [3.0, 1.0, 0.2]

print softmax(scores)

print softmax2(scores)


