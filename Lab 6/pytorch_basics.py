import torch

# Create tensors
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

print('Tensor A:', a)
print('Tensor B:', b)
print('Addition:', a + b)
print('Multiplication:', a * b)
print('Dot Product:', torch.dot(a, b))

matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print('\nMatrix:\n', matrix)
print('Shape:', matrix.shape)
print('Transpose:\n', matrix.T)
