#####################
#Ultimate ANOVA file#
#####################

import numpy as np
from csv_to_datalist import *
from datagen import *

def many_means(data):
#input: list of lists
#output: mean of each list in the data
    l = len(data)
    xs = []
    i = 0
    while i < l:
        xs.append(np.mean(data[i]))
        i += 1
    return xs

def overall_mean(data):
#input: data list
#output: mean over all records in the data
    l = len(data)
    flat_list = [item for sublist in data for item in sublist] #list-of-lists to list
    overall_mean = np.mean(flat_list)
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

def fstar(n, dfa, dfe, mse, noise):
#input: sample size, degrees of freedom, and amount of noise
#output: n random variables drawn from chisquare with noise added
    numerator = (mse*np.random.chisquare(dfa, n) + noise)/(dfa)
    denominator = (mse*np.random.chisquare(dfe, n) + noise)/(dfe)
    return numerator/denominator

def pval(f, n, dfa, dfe, mse, noise):
    fstarsim = fstar(n, dfa, dfe, mse, noise)
    return np.mean(fstarsim > f)

def anova(data, epsilon, n):
#input: normalized data list, epsilon (or None), number of runs n
#output: epsilon-differentially private f-ratio, SSA, SSE, MSA, MSE in dictionary
    number_of_groups = len(data)
    total_size = sum([len(data[i]) for i in range(len(data))])
    dfa = number_of_groups - 1
    dfe = total_size - number_of_groups
    fvals = []
    ssavals = []
    ssevals = []
    msevals = []
    if epsilon == None:
        sse = SSE(data, None)
        ssa = SSA(data, None)
        msa = ssa / dfa
        mse = sse / dfe
        f = msa / mse
        fvals.append(f)
        ssavals.append(ssa)
        ssevals.append(sse)
        msevals.append(mse)
    else:
        i = 0
        while i < n:
            sse = SSE(data, epsilon / 2)
            ssa = SSA(data, epsilon / 2)
            msa = ssa / dfa
            mse = sse / dfe
            f = msa / mse
            fvals.append(f)
            ssavals.append(ssa)
            ssevals.append(sse)
            msevals.append(mse)
            i += 1
    return {'f':fvals, 'ssa':ssavals, 'sse':ssevals, 'mse':msevals}

def error(actual, expected):
    return (abs(actual - expected)/expected)*100
