import numpy as np

def mean(xs):
    n = len(xs)
    x = 0
    i = 0
    while i < n:
        x = x + xs[i]
        i += 1
    return float(x)/n

def many_means(ys):
    n = len(ys)
    xs = []
    i = 0
    while i < n:
        m = mean(ys[i])
        xs.append(m)
        i += 1
    return xs

def overall_mean(ys):
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
    x = mean(xs)
    return x

def SSA(xs, ys, m):
    if len(xs) != len(ys):
        return False
    else:
        n = len(xs)
        x = 0
        i = 0
        while i < n:
            x = x + xs[i]*((ys[i] - m)**2)
            i += 1
        s = x
        return s

def SSE(xs, ys):
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
        s = x
        return s

def anova3(data):
    xs = []
    for i in data:
        xs.append(data[i])
    number_of_groups = len(xs)
    group_means = many_means(xs)
    mean = overall_mean(xs)
    sizes = [len(xs[i]) for i in range(len(xs))]
    total_size = sum(sizes)
    sse = SSE(xs, group_means) + np.random.laplace(0.0, 3/(epsilon/2.0))
    ssa = SSA(sizes, group_means, mean) + np.random.laplace(0.0, 3/(epsilon/2.0))
    dfe = total_size - number_of_groups
    dfa = number_of_groups - 1
    mse = sse/dfe
    msa = ssa/dfa
    f = msa/mse
    return f

