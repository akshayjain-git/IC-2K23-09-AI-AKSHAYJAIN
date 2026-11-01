import torch
import torch.nn.functional as F
from torchvision import models

# Load a pretrained CNN model
model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.eval()

activations = []
gradients = []

def forward_hook(module, input, output):
    activations.append(output)

def backward_hook(module, grad_input, grad_output):
    gradients.append(grad_output[0])

layer = model.layer4[-1]
layer.register_forward_hook(forward_hook)
layer.register_full_backward_hook(backward_hook)

# Example input image tensor
image = torch.randn(1, 3, 224, 224)
output = model(image)
class_index = output.argmax(dim=1).item()

model.zero_grad()
output[0, class_index].backward()

weights = gradients[0].mean(dim=(2, 3), keepdim=True)
cam = (weights * activations[0]).sum(dim=1, keepdim=True)
cam = F.relu(cam)
cam = F.interpolate(cam, size=(224, 224), mode='bilinear', align_corners=False)
cam = cam - cam.min()
cam = cam / (cam.max() + 1e-8)

print('Predicted class index:', class_index)
print('Grad-CAM heatmap shape:', cam.shape)
