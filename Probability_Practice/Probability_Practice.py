import numpy as np
import scipy.stats as sc
import matplotlib.pyplot as plt


def consecutive(data, stepsize = 0):
    return np.split(data, np.where(np.diff(data) != stepsize)[0]+1)

def getData(X):
    Y = np.array([])
    counter = 0
    for lst in X:
        add_one = False
        for con in consecutive(lst):
            if len(con) >= counter and con[0] == 1:
                add_one = True
                continue
        Y = np.append(Y, 1) if add_one else np.append(Y, 0)
        counter += 1
    return Y

def plot(axrow, y, i):
    axrow[i].plot(y, '.', color = 'red')

def main(k, trials):
    NUM = 2**k # number of sample points
    # number of rows in plot
    nrows = trials/2 + 1 if trials%2 == 1 else trials/2 
    fig, axes = plt.subplots(nrows, 2)
    
    counter = 0.0 
    for row in axes:   
        for j in xrange(2):
            X = np.array([sc.bernoulli.rvs(counter/(trials-1)) for n in xrange(NUM)])
            X_split = np.split(X, [2**i for i in xrange(k)])
            Y = getData(X_split)
            plot(row, Y, j)
            counter += 1 
    plt.show()

if __name__ == '__main__':
    trials = 20 # number of trials
    size = 10 # for 2**size
    ''' 
    Plots how points A_k changes as probability
    evenly changes from 0 to 1 with increments
    as number of trials.
    '''
    main(size, trials)