import numpy as np
from sklearn.decomposition import PCA

X = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0]
])

# PCA
pca = PCA(n_components=1)
X_pca = pca.fit_transform(X)

print('PCA Result:\n', X_pca)
print('Explained Variance Ratio:', pca.explained_variance_ratio_)

# SVD
U, S, VT = np.linalg.svd(X, full_matrices=False)

print('\nU Matrix:\n', U)
print('\nSingular Values:\n', S)
print('\nVT Matrix:\n', VT)
