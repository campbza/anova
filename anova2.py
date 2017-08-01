import numpy as np
from anova1 import *

def anova2(data, epsilon, delta):
    xs = []
    for i in data:
        xs.append(data[i])
    means = [mean(xs[i]) for i in range(len(xs))]
    ys = []
    for i in range(len(xs)):
        ys + xs[i]
    overall_mean = mean(ys)
    sizes = [len(xs[i]) for i in range(len(xs))]
    sse = 
    ssa = 
    dfa = 
    dfe = 
    mse = 
    msa = 
    f = 
    return 
