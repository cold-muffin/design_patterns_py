
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, data:any):
        "Handle an event"

class SMSNotifier(Observer):
    def update(self, data):
         print(f"The value of {data["name"]} changed to from {data["old_value"]} to {data["new_value"]}")

class EmailNotifier(Observer):
    def update(self, data):
        print(f"from: @{data["name"]} | content: Value changed from {data["old_value"]} to {data["new_value"]}")

# This class does violate SRP, but it is structured like this for the simplicity of this example
class Product:
    def __init__(self, name, value):
        self.name = name
        self.old_value = None
        self.value = value
        self.observers = []

    def attach_observers(self, *args:Observer):
        self.observers.extend(args)

    def detach_observers(self, *args:Observer):
        for observer in args:
            self.observers.remove(observer)

    def update_observers(self, data:any):
        for observer in self.observers:
            observer.update(data=data)
    
    def set_value(self, new_val):
        self.old_value = self.value
        self.value = new_val
        self.update_observers(data={"name": self.name, "old_value": self.old_value, "new_value": self.value})


if __name__ == "__main__":

    # Create observers
    sms = SMSNotifier()
    email = EmailNotifier()

    # Create product and attach observers
    product = Product("Yak Razor", 500)
    product.attach_observers(sms, email)

    another_product = Product("Rubber Duck", 0)
    another_product.attach_observers(sms)

    # This should alert SMS and Email observers
    product.set_value(100)

    # This should only alert the SMS observer
    another_product.set_value(1000)

    # This should alert no observers
    product.detach_observers(sms, email)
    product.set_value(0)