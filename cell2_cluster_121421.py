import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import cluster_tools as ct


# Read Cell 1 Params and process
cell2_LOGParams = pd.read_csv('../cell2_LOGParams_hofAll_121421.txt', sep=' ')
fitness = cell2_LOGParams.iloc[:, 14]
params = cell2_LOGParams.iloc[:, 0:13]
scaler = StandardScaler()
scl_data = scaler.fit_transform(params)

Z = ct.get_Z_ward(scl_data)
k, sse = ct.plot_kmeans_knee(scl_data, max_k=20, return_sse=True)  # k=6
ksc, sc = ct.plot_kmeans_silhouette_coeff(scl_data, max_k=20, return_SC=True)  # k=12

ct.plot_dendrogram(Z)

ct.plot_dendrogram(Z, max_d=14.0)

k12_clstrs = ct.get_clstrs_k(Z, max_k=12)
clstrs_df = pd.DataFrame(data=cell2_clstrs, columns=['clstrs'])
# singular cluster k=12
clstrs_df.to_csv('./cell2_clstrs_k11_121421.txt', sep=' ', index=False)

k8_clstrs = ct.get_clstrs_k(Z, max_k=8)
clstrs_df = pd.DataFrame(data=cell2_clstrs, columns=['clstrs'])

# Check for singular clusters
clstr_counts = np.bincount(cell2_clstrs)[1:]
