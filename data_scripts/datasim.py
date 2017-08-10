import numpy as np

def fstar(n, eps, k, N):
    numerator = (np.random.chisquare(k - 1, n) + np.random.laplace(0.0, 3.0/eps, n))/(k - 1)
    denominator = (np.random.chisquare(N - k, n) + np.random.laplace(0.0, 3.0/eps, n))/(N - k)
    return numerator/denominator


