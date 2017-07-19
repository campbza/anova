import csv

def f(x, c1, c2):

#input: csv file x, column c1 (categorical variable), column c2 (response variable)
#output: dictionary where key is categorical variable, value is response variable

	with open(x, mode = 'r') as infile:
		data = [(row[c1],float(row[c2])) for row in csv.DictReader(infile)]
	dict = {}
	for k,v in data:
		if k in dict:
			dict[k].append(v)
		else:
			dict[k] = [v]
	return dict

