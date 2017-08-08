import csv

def normalize(xs):
    n = len(xs)
    maximum = max([max(xs[i]) for i in range(n)])
    ys = xs
    for i in range(n):
        l = len(xs[i])
        for j in range(l):
            ys[i][j] = xs[i][j] / float(maximum)
    return ys

def f(x, c1, c2):
#input: csv file x, column c1 (categorical variable), column c2 (response variable)
#output: dictionary where key is categorical variable, value is response variable
    with open(x, mode = 'r') as infile:
	    data = [(row[c1],row[c2]) for row in csv.DictReader(infile)]
    dict = {}
    for k,v in data:
	    if k in dict:
		    dict[k].append(v)
	    else:
		    dict[k] = [v]
    for i in dict:
        dict[i] = filter(None, dict[i])
    for i in dict:
        for j in range(len(dict[i])):
            dict[i][j] = float(dict[i][j])
    xs = [dict[i] for i in dict]
    data = normalize(xs)
    return data


