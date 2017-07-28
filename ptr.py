import numpy as np

def cdf(x, m, b):
    if x < m:
        return (1.0/2.0)*np.exp((x-m)/b)
    else:
        return 1.0 - (1.0/2.0)*np.exp((-x-m)/b)

def noisy_size_estimate(data, epsilon, delta):
    xs = list(data.values())
    m = min([len(xs[i]) for i in range(len(xs))])
    noisy_m = m + np.random.laplace(0.0,1.0/epsilon)
    x = -np.log(2*delta)/epsilon
    working_min = noisy_m - x
    return working_min
