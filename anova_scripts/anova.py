#####################
#Ultimate ANOVA file#
#####################

import numpy as np
from csv_to_datalist import *

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

def many_means(data):
#input: data list
#output: mean of each list in the data
    l = len(data)
    xs = []
    i = 0
    while i < l:
        m = mean(data[i])
        xs.append(m)
        i += 1
    return xs

def overall_mean(data):
#input: data list
#output: mean over all records in the data
    l = len(data)
    flat_list = [item for sublist in data for item in sublist] #list-of-lists to list
    overall_mean = mean(flat_list)
    return overall_mean
    

def SSA(data, epsilon):
#input: data list, epsilon value (optional)
#output: epsilon-differentially private SSA
    l = len(data)
    sizes = [len(data[i]) for i in range(l)]
    means = many_means(data)
    mean = overall_mean(data)
    ssa = 0
    i = 0
    while i < l:
        ssa += sizes[i] * ((means[i] - mean) ** 2)
        i += 1
    if epsilon == None:
        return ssa
    else:
        ssa += np.random.laplace(0.0, 3.0/epsilon) # 3 is sensitivity of SSA
        return ssa

def SSE(data, epsilon):
#input: data list, epsilon value
#output: epsilon-differentially private SSE
    l = len(data)
    means = many_means(data)
    sse = 0
    i = 0
    while i < l:
        m = len(data[i])
        x = 0
        j = 0
        while j < m:
            x += (data[i][j] - means[i]) ** 2
            j += 1
        sse += x
        i += 1
    if epsilon == None:
        return sse
    else:
        sse += np.random.laplace(0.0, 3.0/epsilon) # 3 is sensitivity of SSE
        return sse

def fstar(n, dfa, dfe, noise):
#input: sample size, degrees of freedom, and amount of noise
#output: n random variables drawn from chisquare with noise added
    numerator = (np.random.chisquare(dfa, n) + noise)/(dfa)
    denominator = (np.random.chisquare(dfe, n) + noise)/(dfe)
    return numerator/denominator

def anova(data, epsilon):
#input: normalized data list, epsilon (or None)
#output: epsilon-differentially f-ratio, SSE and SSA
    number_of_groups = len(data)
    total_size = sum([len(data[i]) for i in range(len(data))])
    dfa = number_of_groups - 1
    dfe = total_size - number_of_groups
    if epsilon == None:
        sse = SSE(data, None)
        ssa = SSA(data, None)
        fstarsim = fstar(1000000, dfa, dfe, 0) #simulated distribution under zero noise 
    else:
        sse = SSE(data, epsilon / 2)
        ssa = SSA(data, epsilon / 2)
        fstarsim = fstar(1000000, dfa, dfe, np.random.laplace(0.0, 3.0/epsilon, 1000000)) #simulated distribution with nosie ~ Lap(3/epsilon)
    msa = ssa / dfa
    mse = sse / dfe
    f = msa / mse
    pval = mean(fstarsim > f) # amount of data in the sample distribution that is more extreme than what we witness
    return f, ssa, sse, pval

