import torch
import torch.nn as nn

# Simple model for demonstrating FGSM
model = nn.Sequential(
    nn.Linear(4, 8),
    nn.ReLU(),
    nn.Linear(8, 3)
)

x = torch.tensor([[0.2, 0.4, 0.6, 0.8]], requires_grad=True)
target = torch.tensor([1])

criterion = nn.CrossEntropyLoss()
output = model(x)
loss = criterion(output, target)

model.zero_grad()
loss.backward()

# Fast Gradient Sign Method
epsilon = 0.1
perturbed_x = x + epsilon * x.grad.sign()
perturbed_x = torch.clamp(perturbed_x, 0, 1)

print('Original Input:', x.detach())
print('Gradient:', x.grad)
print('Adversarial Input:', perturbed_x.detach())
