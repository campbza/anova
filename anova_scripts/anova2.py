import numpy as np
from anova1 import *

def mean(xs):
    n = len(xs)
    x = 0
    i = 0
    while i < n:
        x = x + xs[i]
        i += 1
    return float(x)/n

def many_means(xs):
    n = len(xs) 
    ys = []
    i = 0
    while i < n:
        m = mean(xs[i])
        ys.append(m)
        i += 1
    return ys

def overall_mean(xs):
    n = len(xs)
    ys = []
    i = 0
    while i < n:
        l = len(xs[i])
        j = 0
        while j < l:
            ys.append(xs[i][j])
            j += 1
        i += 1
    x = mean(ys)
    return x

def SSA(sizes, means, mean):
    if len(sizes) != len(means):
        return False
    else:
        n = len(sizes)
        x = 0
        i = 0
        while i < n:
            x = x + sizes[i]*((means[i] - mean)**2)
            i += 1
        return x

def SSE(xs, means):
    if len(xs) != len(means):
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
                y = y + (xs[i][j] - means[i])**2
                j += 1
            x = x + y
            i += 1
        return x

def normalize(xs):
    n = len(xs)
    ys = [max(xs[i]) for i in range(n)]
    maximum = max(ys)
    zs = xs
    for i in range(n):
        for j in range(len(xs[i])):
            zs[i][j] = xs[i][j]/float(maximum)
    return zs

def anova2(data, epsilon):
    xs = []
    for i in data:
        xs.append(data[i])
    xs = normalize(xs)
    number_of_groups = len(xs)
    group_means = many_means(xs)
    mean = overall_mean(xs)
    sizes = [len(xs[i]) for i in range(len(xs))]
    total_size = sum(sizes)
    sse = SSE(xs, group_means) + np.random.laplace(0.0, 3.0/(epsilon/2.0))
    ssa = SSA(sizes, group_means, mean) + np.random.laplace(0.0, 3.0/(epsilon/2.0))
    dfe = total_size - number_of_groups
    dfa = number_of_groups - 1
    mse = sse/dfe
    msa = ssa/dfa
    f = msa/mse
    return f
