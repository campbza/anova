import csv

def convert(infile, outfile):
	with open(infile) as fin, open(outfile, 'w') as fout:
		o = csv.writer(fout)
		for line in fin:
			o.writerow(line.split())


