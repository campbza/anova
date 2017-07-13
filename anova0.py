import numpy

def mean(xs):
    n = len(xs)
    x = 0
    i = 0
    while i < n:
        x = x + xs[i]
        i = i + 1
    return float(x)/n

def many_means(ys):
    n = len(ys)
    i = 0
    xs = []
    while i < n:
        m = mean(ys[i])
        xs.append(m)
        i = i + 1
    return xs

#sum of squares formulas
def SST(xs,m):
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
    return x
            

#def SSA():

#def SSE():

#mean squares formulas
#def MSA():

#def MSE():




