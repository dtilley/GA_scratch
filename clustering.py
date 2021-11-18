""" This is example code for clustering algorithms. """

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import numpy as np
import matplotlib.pyplot as plt
from kneed import KneeLocator


"""Create sample data with make_blobs. Returns a tuple of
length 2 (ndarray(data), ndarray(category))
The first clustering algorithm tested is KMeans."""
# I chose to have 3D data for fun
data, clstr = make_blobs(n_samples=200, n_features=3, centers=4,
                         cluster_std=1.6, random_state=5)

ax = plt.axes(projection='3d')
ax.scatter3D(xs=data[:, 0], ys=data[:, 1], zs=data[:, 2], c=clstr)
plt.show()

# Create kmeans object
kmeans = KMeans(n_clusters=4, init='k-means++', n_init=10)

""" Since make_blobs creates normally-distributed data StandardScaler
should work well for preprocessing"""
scaler = StandardScaler()
scl_data = scaler.fit_transform(data)

# fit kmeans object to data
kmeans.fit(scl_data)

# Check some algorithm details
# The lowest SSE
kmeans.inertia_

# The cluster centers
kmeans.cluster_centers_

# The number of iterations for the final (lowest SSE) centers to converge
kmeans.n_iter_

# Predict cluster groupings
# *Note that predicted cluster labels are different than labels produced by make_blobs
kmeans.labels_[:5]
clstr[:5]

ax = plt.axes(projection='3d')
ax.scatter3D(xs=data[:, 0], ys=data[:, 1], zs=data[:, 2], c=kmeans.labels_)
plt.show()

# Choosing appropriate number of clusters using the elbow method
kmeans_kwargs = {
    'init': 'k-means++',
    'n_init': 10,
    'max_iter': 300,
}

sse = []  # SSE is the sum of each data point to its associated cluster
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(scl_data)
    sse.append(kmeans.inertia_)
k = np.arange(1, 11)
kl = KneeLocator(k, sse, curve='convex', direction='decreasing')
kl.plot_knee()
plt.show()
# the number of clusters to choose is located at the elbow
kl.elbow  # 3 in this case

# Choosing appropriate number of clusters using the silhouette coefficient

silhouette_coefficients = []  # silhouette coefficient requires >=2 clusters
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)
    kmeans.fit(scl_data)
    score = silhouette_score(scl_data, kmeans.labels_)
    silhouette_coefficients.append(score)
# the number of clusters to choose is the maximum silhouette coefficient
k[silhouette_coefficients.index(max(silhouette_coefficients))]  # Here: 4


""" Test the Agglomerative Clustering Method """

from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

# Calculate the linkage between data points
Z = linkage(scl_data, 'ward')  # the ward method is bottom -> up euclidean
# The format of Z; rows: n-1, columns: indx1, indx2, dist, n_individuals

"""Check if the actual pairwise distances of all your samples to the distance
implied by the hierarchical clustering using the cophenet correlation
coefficient."""
from scipy.cluster.hierarchy import cophenet
from scipy.spatial.distance import pdist

c, coph_dists = cophenet(Z, pdist(scl_data)) # c is the correlation coefficient

# Calculate full dendrogram
plt.figure()
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(Z,
           truncate_mode='lastp',
           p=12,  # Only show final 12 merges (horizontal lines)
           leaf_rotation=90.0,
           leaf_font_size=8.0)
plt.show()

# Select the number of clusters
from scipy.cluster.hierarchy import fcluster

# Using a distance cutoff
nclusters = fcluster(Z, t=5.0, criterion='distance')



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
