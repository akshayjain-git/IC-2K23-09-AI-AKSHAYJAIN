import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
print("Shape:", arr.shape)
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Sum:", np.sum(arr))

matrix = np.array([[1, 2], [3, 4]])
print("\nMatrix:\n", matrix)
print("Transpose:\n", matrix.T)
print("Matrix multiplication:\n", np.dot(matrix, matrix))
