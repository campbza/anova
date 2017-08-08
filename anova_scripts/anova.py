#####################
#Ultimate ANOVA file#
#####################

import numpy as np
from csv_to_dict import *

def mean(xs):
#input: list of values
#output: real-valued mean
    n = len(xs)
    x = 0
    i = 0
    while i < n:
        x += xs[i]
        i += 1
    return float(x) / n

def many_means(data, epsilon):
#input: data list, epsilon (optional), min_size_est (optional)
#output: list of means of each list in the data, or epsilon-differentially private list of means of each list in the data, or epsilon-delta-differentially private means of each list in the data
    n = len(data)
    xs = []
    i = 0
    if epsilon == None:
        while i < n:
            m = mean(data[i])
            xs.append(m)
            i += 1
        return xs
    else:
        while i < n:
            m = mean(data[i])
            xs.append(m + np.random.laplace(0.0, 1.0/epsilon))
            i += 1
        return xs

def overall_mean(data, epsilon):
#input: data list, epsilon value
#output: epsilon-differentially private mean of the whole dataset
    n = len(data)
    xs = []
    i = 0
    while i < n:
        l = len(data[i])
        j = 0
        while j < l:
            xs.append(data[i][j])
            j += 1
        i += 1
    x = mean(xs)
    if epsilon == None:
        return x
    else:
        x += np.random.laplace(0.0, 2.0/((n-1)*epsilon))
        return x

def SSA(data, epsilon):
#input: data list, epsilon value
#output: epsilon-differentially private SSA
    n = len(data)
    sizes = [len(data[i]) for i in range(n)]
    means = many_means(data, None)
    mean = overall_mean(data, None)
    ssa = 0
    i = 0
    while i < n:
        ssa += sizes[i] * ((means[i] - mean) ** 2)
        i += 1
    if epsilon == None:
        return ssa
    else:
        ssa += np.random.laplace(0.0, 3.0/epsilon)
        return ssa

def SSE(data, epsilon):
#input: data list, epsilon value
#output: epsilon-differentially private SSE
    n = len(data)
    means = many_means(data, None)
    sse = 0
    i = 0
    while i < n:
        l = len(data[i])
        x = 0
        j = 0
        while j < l:
            x += (data[i][j] - means[i]) ** 2
            j += 1
        sse += x
        i += 1
    if epsilon == None:
        return sse
    else:
        sse += np.random.laplace(0.0, 3.0/epsilon)
        return sse

def anova(data, epsilon):
    number_of_groups = len(data)
    total_size = sum([len(data[i]) for i in range(len(data))])
    dfa = number_of_groups - 1
    dfe = total_size - 1
    if epsilon == None:
        sse = SSE(data, None)
        ssa = SSA(data, None)
    else:
        sse = SSE(data, epsilon / 2)
        ssa = SSA(data, epsilon / 2)
    msa = ssa / dfa
    mse = sse / dfe
    f = msa / mse
    return f

