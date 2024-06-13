'''What is the usage of super() in class init method?'''

# specify which method to call from in a hierarchical class definition
class Rectangle :
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def area (self):
        print ("Calculate from Rectangle!")
        return self.height*self.width
    
class Square (Rectangle) :
    def __init__(self, side) -> None:
        super(Square, self).__init__(side, side)     # the same to super().__init__()

    def area (self):
        print("Calculate from Square!")
        return super(Square, self).area()            # similar to return super().area()
    
class Cube (Square) :
    def __init__(self, side) -> None:
        super().__init__(side)

    def surface_area_from_rect (self):
        return super(Square, self).area()
    
    def surface_area_from_square (self):
        return super(Cube, self).area()

# if (__name__ == "__main__"):
#     cube = Cube(5)
#     print(cube.surface_area_from_rect())            # invoke the area method in Rectangle
#     print(cube.surface_area_from_square())          # invoke the area method in Square, which invoke the area method in Rectangle

# super() in multiple inheritance

'''
Dilation
Visualization: https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md
'''
import torch
from torch import Tensor
from torch import nn

# dilation = 1 ~ normal convolution
RANDOM_SEED = 42
torch.manual_seed(RANDOM_SEED)
n_channels = 2

in_tensor = torch.randint(low = 0, high=5, size=(n_channels, 5, 5), dtype=torch.float32) 

print(f"\033[1m Input Tensor:\033[0m {in_tensor}")
print(f"shape = {in_tensor.shape}")
conv = nn.Conv2d(in_channels=n_channels, out_channels=2, kernel_size=3, stride=1, dilation=1)
out_tensor = conv(in_tensor)
print(f"\033[1m Output Tensor:\033[0m {out_tensor}")
print(f"shape = {out_tensor.shape}")

# dilation = 2
conv_dilate = nn.Conv2d(in_channels=n_channels, out_channels=1, kernel_size=3, stride=1, dilation=2)
out_tensor_dilate = conv_dilate(in_tensor)
print(f"\033[1m Output Tensor \033[0m (dilation = 2): {out_tensor_dilate}")
print(f"shape = {out_tensor_dilate}")