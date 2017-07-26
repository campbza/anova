import numpy as np

def noisy_size_estimate(data, lb, epsilon, delta):
    xs = [len(data[i]) for i in range(len(data))]
    noisy_xs = [abs(i + np.random.laplace(0.0,1.0/epsilon)) for i in xs]
    noisy_min = min(noisy_xs)
    d = abs(lb - noisy_min)
    cdf = 1 - 1/2 * exp(- d/(1.0/epsilon))
    
