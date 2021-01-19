import numpy as np
import skfuzzy as fuzz

class cluster():

  # initialize the class:
  # find the cluster center values and assign each grid point to each cluster
  # cluster center values are not necessarily sorted

  # outputs:
    # cntr is the value of the center of the clusters (i.e. the characteristic velicity of UMZs)
    # u is the final fuzzy c-partitioned matrix: it shows how well each data point belongs to certain clusters
     # e.g u[ii,jj,:] = [0, 0.2, 0.9, 0.3] shows U[ii,jj] belongs to
     # clusters 1, 2, 3, and 4 with the probablity of 0, 20, 90, and 30 percent, respectively.
     # so u[ii,jj] belongs to cluster 3 (with the highest probablity)
  def __init__(self,x,y,U,n_clusters):
    data = np.reshape(U,(1,-1))
    cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(data,n_clusters,2,error=0.0001, maxiter=10000, init=None)
    self.labels = np.reshape(np.argmax(u,axis=0),U.shape)
    self.labels = self.relabel(self.labels,cntr,n_clusters)
    self.ys = self.get_ys(self.labels,y,n_clusters)

  # label each grid point to indicate the cluster number it belongs to
    # labels is a matrix with the shape of U, each element of which shows which cluster that grid point belongs to:
    # e.g labels[ii,jj] = 3. Passing through relabel: number of clusters are ascending according to their u values
  # Sort the cluster center values from low to high, then sort the labels accordingly
  def relabel(self,label,center,n_clusters):
    tmp = np.linspace(0,n_clusters-1,n_clusters,dtype=np.int)
    center,tmp = zip(*sorted(zip(center,tmp)))
    xx,yy = np.shape(label)
    mask = np.zeros((xx,yy,n_clusters))
    for ii in range(n_clusters):
        mask[:,:,ii] = label == tmp[ii]
    for ii in range(n_clusters):
        label[np.nonzero(mask[:,:,ii])] = ii+1
    return label

  # get the y location of the border between UMZs
  def get_ys(self,label,y,n_clusters):
    nx,ny = label.shape
    ys = np.zeros((nx,n_clusters-1))
    for n in range(n_clusters-1):
      for ii in range(nx):
        ytmp = np.array([])
        for jj in range(ny-1):
          if (label[ii,jj] == n+2 and label[ii,jj+1] == n+1) or (label[ii,jj] == n+1 and label[ii,jj+1] == n+2):
              ytmp = np.append(ytmp,0.5*(y[jj]+y[jj+1]))
        if len(ytmp) != 0:
            ys[ii,n] = np.max(ytmp)
        else:
            ys[ii,n] = 0
    return ys
