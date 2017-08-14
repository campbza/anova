import numpy as np

def datagen(range1, range2, range3, n1, n2, n3):
#input: ranges in the form [a,b] where a<b in (0,1), and 3 sample sizes for each generated list
#output: datalist populated with 3 groups of data
    data1 = [np.random.uniform(range1[0], range1[1]) for i in range(n1)]
    data2 = [np.random.uniform(range2[0], range2[1]) for i in range(n2)]
    data3 = [np.random.uniform(range3[0], range3[1]) for i in range(n3)]
    data = [data1, data2, data3]
    return data

def sample(data, samplesize):
#input: data (format: list of three lists), and a sampling size
#output: datalist populated with 3 groups, each of size "samplesize", sampled from each list, no replacement
    sample1 = np.array(np.random.choice(data[0], samplesize, replace = False)).tolist()
    sample2 = np.array(np.random.choice(data[1], samplesize, replace = False)).tolist()
    sample3 = np.array(np.random.choice(data[2], samplesize, replace = False)).tolist()
    sample_data = [sample1, sample2, sample3]
    return sample_data

