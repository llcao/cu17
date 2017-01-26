import numpy as np
from numpy import random

def pegasos_svm(xs, ys, opt_lambda, nepoch):
    t = 1
    m, d = xs.shape
    assert m == len(ys)
    w = np.zeros((d,))
    for it in range(nepoch):
        sample_inds = random.permutation(range(m))
        for tau in sample_inds:
            if np.dot(xs[tau,:], w) * ys[tau] < 1:
                # data too close or wrongly separated
                w = (1-1.0/t) * w + 1.0/opt_lambda/t * ys[tau] * xs[tau,:]
            else:
                # correctly separated
                w -= w / t
            t += 1
    return w

xs0 = np.array([[3.0, 2.0],[2.0, 3.0]])
ys0 = np.array([1, -1])
print pegasos_svm(xs0, ys0, 0.1, 10)

