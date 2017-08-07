import csv

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
            for j in dict[i]:
                dict[i][j] = float(dict[i][j])
	return dict

