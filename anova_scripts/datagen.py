import numpy as np

def datagen(m1, m2, m3, v, n):
#input: 0.35, 0.5, 0.65, v = 0.15
#output: 
    data1 = np.array(np.random.normal(m1, v, n)).tolist()
    data2 = np.array(np.random.normal(m2, v, n)).tolist()
    data3 = np.array(np.random.normal(m3, v, n)).tolist()
    data = [data1, data2, data3]
    k = len(data)
    i = 0
    while i < k:
        l = len(data[i])
        j = 0
        while j < l:
            if data[i][j] > 1.0:
                data[i][j] = 1.0
            elif data[i][j] < 0.0:
                data[i][j] = 0.0
            j += 1
        i += 1
    return data

def sample(data, samplesize):
#input: data (format: list of three lists), and a sampling size
#output: datalist populated with 3 groups, each of size "samplesize", sampled from each list, no replacement
    sample1 = np.array(np.random.choice(data[0], samplesize, replace = False)).tolist()
    sample2 = np.array(np.random.choice(data[1], samplesize, replace = False)).tolist()
    sample3 = np.array(np.random.choice(data[2], samplesize, replace = False)).tolist()
    sample_data = [sample1, sample2, sample3]
    return sample_data

