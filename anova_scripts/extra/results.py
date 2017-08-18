#epsilon0 = None, epsilon1 = 1.0, epsilon2 = 0.5, epsilon3 = 0.1
#m1 = 0.35, m2 = 0.50, m3 = 0.65, var = 0.15

import matplotlib.pyplot as plt

sizes = [300, 1500, 3000, 9000, 12000]

epsilon0 = [1.0,1.0,1.0,1.0, 1.0]
epsilon1 = [0.735,0.995,1.0,1.0, 1.0]
epsilon2 = [0.605,0.92,.985,1.0, 1.0]
epsilon3 = [0.52,0.58,0.645,0.94,1.0]


def plot_lines():
    x_vals = sizes
    y_vals = [epsilon0, epsilon1, epsilon2, epsilon3]
    labels = ['epsilon = None', 'epsilon = 1.0', 'epsilon = 0.5', 'epsilon = 0.1']
    colors = ['r', 'g', 'b', 'y']
    fig = plt.figure(figsize=(5,5))
    ax = plt.subplot(1,1,1)
    for i in range(len(y_vals)):
        style_code = '-'+colors[i]
        ax.plot(x_vals,y_vals[i],style_code,label=labels[i],lw=2)
    ax.set_xlim([0, 12010])

    plt.title('Differentially private ANOVA')
    plt.xlabel('Database size')
    plt.ylabel('Percent significance')
    plt.legend(loc='lower right')

    plt.tight_layout()
    plt.savefig('results.png')
    print('Wrote to results.png')
    return

if __name__ == '__main__':
    plot_lines()
