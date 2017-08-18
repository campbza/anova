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

def fstar(n, dfa, dfe, mse, epsilon):
#input: sample size, degrees of freedom, and amount of noise
#output: n random variables drawn from chisquare with noise added
    if epsilon != None:
        numerator = (mse*np.random.chisquare(dfa, n) + np.random.laplace(0.0, 3.0/(epsilon/2.0), n))/(dfa)
        denominator = (mse*np.random.chisquare(dfe, n) + np.random.laplace(0.0, 3.0/(epsilon/2.0), n))/(dfe)
    else:
        numerator = (mse*np.random.chisquare(dfa, n))/(dfa)
        denominator = (mse*np.random.chisquare(dfe, n))/(dfe)
    return numerator/denominator

def anova(data, epsilon, filename):
#input: normalized data (list of lists), epsilon, file to write to
#ouput: epsilon-differentially private sse, ssa, and p-value added to file (along with epsilon)
    number_of_groups = len(data)
    total_size = sum([len(data[i]) for i in range(len(data))])
    dfa = number_of_groups - 1
    dfe = total_size - number_of_groups
    if epsilon == None:
        sse = SSE(data, None)
        ssa = SSA(data, None)
    else:
        sse = SSE(data, epsilon / 2)
        ssa = SSA(data, epsilon / 2)
    mse = sse / dfe
    msa = ssa / dfa
    f = msa / mse
    fstarsim = fstar(1000000, dfa, dfe, 0.0225, epsilon)
    pval = np.mean(fstarsim > f)
    with open(filename, 'a') as fout:
        fout.write(str(total_size) + ',' + str(sse) + ',' + str(ssa) + ',' + str(epsilon) + ',' + str(pval) + ',' + str(f) + '\n')

def anova_test(num_runs, epsilon_vals, filename, m1, m2, m3, var, group_counts):
    i = 0
    while i < len(epsilon_vals):
        j = 0
        while j < len(group_counts):
            k = 0
            while k < num_runs:
                data = datagen(m1,m2,m3,var,group_counts[j])
                anova(data, epsilon_vals[i], filename)
                k += 1
            j += 1
        i += 1
    print('Wrote data to ' + filename)
    return





def significance(filename, threshold):
    with open(filename, 'r') as f:
        data = [float(row['pval']) for row in csv.DictReader(f)]
        n = len(data)
        sig_vals = [item for item in data if item < threshold]
        m = len(sig_vals)
        return float(m)/float(n)

def anova1(data, epsilon):
#input: normalized data(list of lists), epsilon
#output: epsilon-differentially private p-value
    number_of_groups = len(data)
    total_size = sum([len(data[i]) for i in range(len(data))])
    dfa = number_of_groups - 1
    dfe = total_size - number_of_groups
    if epsilon == None:
        sse = SSE(data, None)
        ssa = SSA(data, None)
    else:
        sse = SSE(data, epsilon / 2)
        ssa = SSA(data, epsilon / 2)
    mse = sse / dfe
    msa = ssa / dfa
    f = msa / mse
    if epsilon == None:
        fstarsim = fstar(1000000, dfa, dfe, mse, 0)
        pval = np.mean(fstarsim > f)
    else:
        fstarsim = fstar(1000000, dfa, dfe, mse, np.random.laplace(0.0, 3.0))
        pval = np.mean(fstarsim > f)
    return pval
