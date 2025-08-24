
from typing import Literal
from dataclasses import dataclass
from copy import deepcopy

versions = Literal["lite", "standard", "max"]
colors = Literal["red", "blue", "yellow"]
sizes = Literal["small", "medium", "large"]

@dataclass
class Product:
    version: versions  = "standard"
    color: colors      = "blue"
    size: sizes        = "medium"
    has_warranty: bool = False

    def print_attributes(self):
        print(f"Version: {self.version} | "
              f"Color: {self.color} | "
              f"Size: {self.size} | "
              f"Has warranty: {self.has_warranty}")
        
class ProductBuilder:
    def __init__(self):
        self.obj = Product()

    def set_version(self, version:versions):
        self.obj.version = version
        return self
    
    def set_color(self, color:colors):
        self.obj.color = color
        return self

    def set_size(self, size:sizes):
        self.obj.size = size
        return self

    def set_warranty(self, has_warranty:bool):
        self.obj.has_warranty = has_warranty
        return self
    
    def get_product(self):
        return deepcopy(self.obj)

if __name__ == "__main__":

    # Creating a product by changing the parameters
    obj = Product(
        version="max",
        color="yellow"
    )

    obj.print_attributes()

    # Creating a product with the builder
    builder = ProductBuilder()
    builder.set_version("lite")
    builder.set_color("blue")
    builder.set_size("large")

    custom_obj = builder.get_product()

    # Method chaining
    another_custom_obj = builder.set_color("red").set_warranty(True).get_product()

    # Separate instances
    custom_obj.print_attributes()
    another_custom_obj.print_attributes()