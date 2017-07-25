import numpy as np

def mean(xs):
    n = len(xs)
    x = 0
    i = 0
    while i < n:
        x = x + xs[i]
        i = i + 1
    return float(x)/n

def noisy_many_means(ys,e):
    n = len(ys)
    i = 0
    xs = []
    while i < n:
        m = mean(ys[i])
        #l = len(ys[i])
        xs.append(m + np.random.laplace(0.,1./e))
        i = i + 1
    return xs

def noisy_overall_mean(ys,e):
    n = len(ys)
    xs = []
    i = 0
    while i < n:
        l = len(ys[i])
        j = 0
        while j < l:
            xs.append(ys[i][j])
            j = j + 1
        i = i + 1
    x = mean(xs) + np.random.laplace(0.,2./((n - 1)*e))
    return x

#sum of squares formulas
                                                         
def SST(xs,m,e):
#input: list of lists (each inner list a "group" in the database) of values, mean, epsilon
#output: noisy sum of squares total
    n = len(xs)
    x = 0
    i = 0
    while i < len(xs):
        l = len(xs[i])
        y = 0
        j = 0
        while j < l:
            y = y + (xs[i][j] - m)**2
            j = j + 1
        x = x + y
        i = i + 1
    s = x + np.random.laplace(0.,1/e)
    return s

def SSA(xs,ys,m,e):
#input: list of group sizes, corresponding group means, overall mean, epsilon       
#output: noisy sum of squares treatment           
    if len(xs) != len(ys):
        return False
    else:
        n = len(xs)
        l = min([xs[i] for i in range(n)])
        x = 0
        i = 0
        while i < n:
            x = x + xs[i]*((ys[i] - m)**2)
            i = i + 1
        s = x + np.random.laplace(0.,((1/l)+1)/e)
        return s

def SSE(xs,ys,e):
#input: list of lists of values, corresponding group means, epsilon
#output: noisy sum of squares error
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
                j = j + 1
            x = x + y
            i = i + 1
        s = x + np.random.laplace(0.,1/e)
        return s

def anova(data, epsilon, delta):
    xs = []
    for i in data:
        xs.append(data[i])
    means = noisy_many_means(xs, epsilon/4.0)
    mean = noisy_overall_mean(xs, epsilon/4.0)
    sizes = [len(xs[i]) for i in xs]
    sse = SSE(xs,means,epsilon/4.0)
    ssa = SSA(sizes,means,mean,epsilon/4.0)
    size = sum(sizes)
    dfe = sizes - len(xs)
    dfa = len(xs) -1
    mse = sse/dfe
    msa = ssa/dfa
    f = mse/msa
    return f
