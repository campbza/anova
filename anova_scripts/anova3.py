import numpy as np

def min_size_est(data, epsilon, delta):
    xs = list(data.values())
    m = min([len(xs[i]) for i in range(len(xs))])
    noisy_m = m + np.random.laplace(0.0, 1.0/epsilon)
    x = -np.log(2*delta)/epsilon
    working_min = noisy_m - x
    return working_min

def mean(xs):
    n = len(xs)
    x = 0
    i = 0
    while i < n:
        x = x + xs[i]
        i += 1
    return float(x)/n

def noisy_many_means(ys, min_size, epsilon):
    n = len(ys)
    xs = []
    i = 0
    while i < n:
        m = mean(ys[i])
        xs.append(m + np.random.laplace(0.0, 1.0/(min_size*epsilon)))
        i += 1
    return xs

def noisy_overall_mean(ys, epsilon):
    n = len(ys)
    xs = []
    i = 0
    while i < n:
        l = len(ys[i])
        j = 0
        while j < l:
            xs.append(ys[i][j])
            j += 1
        i += 1
    x = mean(xs) + np.random.laplace(0.0, 2.0/((n-1)*epsilon))
    return x

def SSA(xs, ys, m, min_size, epsilon):
    if len(xs) != len(ys):
        return False
    else:
        n = len(xs)
        l = min_size
        x = 0
        i = 0
        while i < n:
            x = x + xs[i]*((ys[i] - m)**2)
            i += 1
        s = x + np.random.laplace(0.0, ((1/l) + 1)/epsilon)
        return s

def SSE(xs, ys, epsilon):
    if len(xs) != len(ys):
        return False
    else:
        n = len(xs)
        x = 0
        i = 0
        while i < n:
            l = len(xs[i])
            y = 0 
            j = 0
            while j < l:
                y = y + (xs[i][j] - ys[i])**2
                j += 1
            x = x + y
            i += 1
        s = x + np.random.laplace(0.0, 1.0/epsilon)
        return s

def normalize(xs):
    n = len(xs)
    ys = [max(xs[i]) for i in range(n)]
    maximum = max(ys)
    zs = xs
    for i in range(n):
        for j in range(len(xs[i])):
            zs[i][j] = xs[i][j]/float(maximum)
    return zs

def anova3(data, epsilon, delta):
    min_size = min_size_est(data, epsilon/4.0, delta)
    xs = []
    for i in data:
        xs.append(data[i])
    xs = normalize(xs)
    number_of_groups = len(xs)
    group_means = noisy_many_means(xs, min_size, epsilon/4.0)
    mean = noisy_overall_mean(xs, epsilon/4.0)
    sizes = [len(xs[i]) for i in range(len(xs))]
    total_size = sum(sizes)
    sse = SSE(xs, group_means, epsilon/4.0)
    ssa = SSA(sizes, group_means, mean, min_size, epsilon/4.0)
    dfe = total_size - number_of_groups
    dfa = number_of_groups - 1
    mse = sse/dfe
    msa = ssa/dfa
    f = msa/mse
    return f
