
class Singleton:
    __shared_instance = None

    def __init__(self):
        if Singleton.__shared_instance:
            raise Exception("Shared instance already exists")
        Singleton.__shared_instance = self
    
    @classmethod
    def get_instance(cls):
        if not cls.__shared_instance:
           cls()
        return cls.__shared_instance
    


if __name__ == '__main__':

    # Create the instance
    obj = Singleton()
    print(obj)

    # Reference the instance with .get_instance()
    ref = Singleton.get_instance()
    print(ref)

    # Attempting to create a second instance
    try:
        another_obj = Singleton()
        print(another_obj)
    except Exception as e:
        print(e)

    # Attempting to create a singleton subclass
    class SubSingleton(Singleton):
        def __init__(self):
            super().__init__()
    
    try:
        another_obj = SubSingleton()
        print(another_obj)
    except Exception as e:
        print(e)