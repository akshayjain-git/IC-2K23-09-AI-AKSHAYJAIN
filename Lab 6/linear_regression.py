import torch
import torch.nn as nn
import torch.optim as optim

X = torch.tensor([[1.0], [2.0], [3.0], [4.0], [5.0]])
y = torch.tensor([[2.0], [4.0], [6.0], [8.0], [10.0]])

model = nn.Linear(1, 1)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

for epoch in range(1000):
    prediction = model(X)
    loss = criterion(prediction, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print('Weight:', model.weight.item())
print('Bias:', model.bias.item())

new_value = torch.tensor([[6.0]])
print('Prediction for x = 6:', model(new_value).item())
