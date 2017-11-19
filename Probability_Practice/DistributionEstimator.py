import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc


def averageDistribution(X, x, N):
    Sn = 0.0
    # Sample Average
    for Xi in X:
        if Xi <= x:    
            Sn += 1
    Fn = Sn / N
    return Fn

def main():
    Nlist = [10, 50, 100, 1000]
    Nsteps = 1000
    i = 1
    for N in Nlist: 
        
        # Normal Parameters
        #mu, sigma = 0.0, 1.0
        #X = np.random.normal(mu, sigma, N)

        # Exponential Parameters
        lmda = 2.2
        X = np.random.exponential(lmda, N)
 
        Xvec = np.linspace(0, 5, Nsteps)
        Yvec = np.array([averageDistribution(X, x, N) for x in Xvec])
    
        # Actual Distribution
        F = sc.expon.cdf(Xvec, scale=lmda)

        plt.subplot(220 + i)
        plt.title('Distribution Estimation For N = %s' %(N,))
        plt.plot(Xvec, Yvec, '.', color = 'red')
        plt.plot(Xvec, F, '-', color = 'black')

        i += 1

    plt.show()        
        

if __name__ == "__main__":
    main()