
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def work(self):
        'Makes a "product" work'

class Product1(Product):
    def work(self):
        print("Product 1 works")

class Product2(Product):
    def work(self):
        print("Product 2 works")

class Product3(Product):
    def work(self):
        print("Product 3 works")

class ProductFactory:
    @staticmethod
    def create_product(product:str, **kwargs) -> Product:
        if product == "product_1":
            return Product1(**kwargs)
        if product == "product_2":
            return Product2(**kwargs)
        if product == "product_3":
            return Product3(**kwargs)
        
if __name__ == "__main__":

    # Create the factory instance
    fac = ProductFactory()

    # Create products without knowing about the original class
    product_1 = fac.create_product("product_1")
    product_1.work()

    product_2 = fac.create_product("product_2")
    product_2.work()