import csv

def convert(infile, outfile):

#input: input space-delimited file, output csv file name
#output: csv file

	with open(infile) as fin, open(outfile, 'w') as fout:
		o = csv.writer(fout)
		for line in fin:
			o.writerow(line.split())


