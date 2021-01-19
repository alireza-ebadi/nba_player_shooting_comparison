import numpy as np
import matplotlib.pyplot as plt
import h5py

from scipy.stats import gaussian_kde

class kde():
    def __init__(self,U):
        # rearrange data into a 1-D array
        data = np.reshape(U,(1,-1))

        xx = np.linspace(np.min(data),np.max(data),500)
        # estimate the pdf based on Gaussian kernel using Scott's rule
        kernel = gaussian_kde(data,bw_method='scott')
        bins = 25
        plt.hist(data.T,bins,normed=True,edgecolor='black',facecolor='white')
        plt.plot(xx,kernel.evaluate(xx),color='k')
        plt.show()
