
from abc import ABC, abstractmethod

# Abstract classes
class Product(ABC):
    @abstractmethod
    def work(self):
        'Makes a "product" work'

class Service(ABC):
    @abstractmethod
    def work(self):
        'Makes a "product" work'

# Products
class ProductStandard(Product):
    def work(self):
        print("Product standard works")

class ProductLite(Product):
    def work(self):
        print("Product lite works a little worse")

# Services
class ServiceStandard(Service):
    def work(self):
        print("Service standard works")

class ServiceLite(Service):
    def work(self):
        print("Service lite works a little worse")

# Abstract factory
class ProductFactory(ABC):
    @abstractmethod
    def create_product(self, version:str, **kwargs):
        "Creates a product's version"
    
    @abstractmethod
    def create_service(self, version:str, **kwargs):
        "Creates a service's version"

# Factories
class StandardFactory(ProductFactory):
    def create_product(self, **kwargs) -> Product:
        return ProductStandard(**kwargs)
    
    def create_service(self, **kwargs) -> Service:
        return ServiceStandard(**kwargs)

class LiteFactory(ProductFactory):
    def create_product(self, **kwargs) -> Product:
        return ProductLite(**kwargs)
    
    def create_service(self, **kwargs) -> Service:
        return ServiceLite(**kwargs)

if __name__ == "__main__":

    # Create factories
    standard_fac = StandardFactory()
    lite_fac = LiteFactory()

    # Create products and services without knowing about the original class
    product_standard = standard_fac.create_product()
    service_standard = standard_fac.create_service()
    product_standard.work()
    service_standard.work()

    product_lite = lite_fac.create_product()
    product_lite.work()