""" This is example code for clustering algorithms. """

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



"""Create sample data with make_blobs. Returns a tuple of 
length 2 (ndarray(data), ndarray(category))
The first clustering algorithm tested is KMeans."""
# I chose to have 3D data for fun
data, clstr = make_blobs(n_samples=200, n_features=3, centers=4, cluster_std=1.6, random_state=5)

# 3D plotting
from mpl_toolkits import mplot3d

ax = plt.axes(projection='3d')
ax.scatter3D(xs=data[:,0], ys=data[:,1], zs=data[:,2], c=clstr)
plt.show()

# Create kmeans object
kmeans = KMeans(n_clusters=4)

# fit kmeans object to data
kmeans.fit(data)

# Predict cluster groupings
# *Note that predicted cluster labels are different than labels produced by make_blobs
c_km = kmeans.fit_predict(data)

ax = plt.axes(projection='3d')
ax.scatter3D(xs=data.iloc[:,0], ys=data.iloc[:,1], zs=data.iloc[:,2], c=c_km)
plt.show()

""" Test the Agglomerative Clustering Method """

import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

# create dendrogram
dendrogram = sch.dendrogram(sch.linkage(data, method='ward'))

# create clusters
hc = AgglomerativeClustering(n_clusters=None, affinity='euclidean', linkage='ward',
                             compute_distances=True, compute_full_tree=True,
                             distance_threshold=0.2)

c_agglo = hc.fit_predict(data)

ax = plt.axes(projection='3d')
ax.scatter3D(xs=data.iloc[:,0], ys=data.iloc[:,1], zs=data.iloc[:,2], c=c_agglo)
plt.show()
