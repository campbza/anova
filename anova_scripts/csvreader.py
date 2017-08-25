import csv
import matplotlib.pyplot as plt

def plot_lines(sizes, eps_vals, significance, outfile, threshold, title):
    x_vals = sizes
    y_vals = significance
    labels = [eps_vals[i] for i in range(len(eps_vals))]
    for i in range(len(labels)):
        labels[i] = 'epsilon = ' + str(labels[i])
    colors = ['r','g','b','y','m','c','k']
    shapes = ['o','s','d','^','x','<','v']
    fig=plt.figure(figsize=(8,5))
    ax=plt.subplot(1,1,1)
    for i in range(len(y_vals)):
        style_code = '-'+colors[i]+shapes[i]
        ax.plot(x_vals,y_vals[i],style_code,label=labels[i],lw=2,ms=8)
    ax.set_xscale('log')
    ax.set_xlim([0,max(x_vals) + 1])
    plt.title(title)
    plt.xlabel('Database size (log scale)')
    plt.ylabel('Percent significance at ' + str(threshold))
    plt.legend(loc='lower right')

    plt.tight_layout()
    plt.savefig(outfile)
    print('Wrote to ' + outfile)
    return

def pvals_significance(infile, outfile, graphtitle, threshold):
#input: csv file, outfile name (.png), graphtitle, and threshold for significant pvals
#output: graph of infile data
    file_contents = open(infile, 'r')
    reader = csv.reader(file_contents)
    pval_dict = {}
    sizes = []
    epsilons = []
    for line in reader:
        size = int(line[0])
        if size not in sizes:
            sizes.append(size) #gather list of sizes (these are total size of the database)
        epsilon = line[3]
        if epsilon not in epsilons:
            epsilons.append(epsilon) #gather list of epsilon values
        key = (size,epsilon)
        if key in pval_dict: #populate dictionary keyed by size,epsilon tuples
            pval_dict[key].append(float(line[4])) #line[4] in csv is the pval
        else:
            pval_dict[key] = [float(line[4])]
    for item in pval_dict: #replace the lists with a percent of how many in that list are significant
        l = len(pval_dict[item])
        sig_pvals = [x for x in pval_dict[item] if x < threshold]
        m = len(sig_pvals)
        pval_dict[item] = float(m) / float(l)
    sizes.sort()
    epsilon_dict = {}
    labels = []
    significance = [] #list of list of percent significance, each list corresponding to epsilon
    for e in epsilons:
        epsilon_dict[e] = []
    for s in sizes:
        for e in epsilons:
            epsilon_dict[e].append(pval_dict[(s,e)])
            if epsilon_dict[e] not in significance:
                significance.append(epsilon_dict[e])
    plot_lines(sizes, epsilons, significance, outfile, threshold, graphtitle)
    return 
