
from copy import deepcopy

class Prototype:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def clone(self):
        "You can return a clone of the object by making a new object with the exact same attributes as the old one (manual copy)"
        return Prototype(self.a, self.b, self.c)

    def pythonic_clone(self):
        "Python already has a built in function to clone objects so the manual copy, and therefore the prototype pattern, is unnecessary"
        return deepcopy(self)
    
    def print_attributes(self):
        print(self, self.__dict__)
    
if __name__ == "__main__":

    # Create object
    obj = Prototype(1.0401, 0.4141, 4.1410)
    obj.print_attributes()

    # Copy object with both methods
    manual_copy = obj.clone()
    manual_copy.print_attributes()

    pythonic_copy = obj.pythonic_clone()
    pythonic_copy.print_attributes()

    # But the prototype pattern is again, unnecessary
    copy = deepcopy(obj)
    print(copy, copy.__dict__)
