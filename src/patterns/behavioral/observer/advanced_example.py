
from abc import ABC, abstractmethod
from dataclasses import dataclass

#===============#
# EVENT CLASSES #
#===============#
@dataclass
class Event:
    name: str
    old_value: int|float
    new_value: int|float

class ValueUpEvent(Event):
    pass

class ValueDownEvent(Event):
    pass

class EventFactory:
    __events = {
        "value_up": ValueUpEvent,
        "value_down": ValueDownEvent
    }

    @classmethod
    def create_set_event(cls, event:str, **kwargs):
        return cls.__events[event](**kwargs)
    
    def create_event(self, name, old_value, new_value):
        if new_value > old_value:
            return self.create_set_event("value_up", name=name, old_value=old_value, new_value=new_value)
        elif new_value < old_value:
            return self.create_set_event("value_down", name=name, old_value=old_value, new_value=new_value)

#==================#
# OBSERVER CLASSES #
#==================#
class Observer(ABC):
    @abstractmethod
    def update(self, event:Event):
        "Handle an event"

class SMSNotifier(Observer):
    def update(self, event):
        if isinstance(event, ValueUpEvent):
            print(f"Good news! {event.name} went up from {event.old_value} to {event.new_value}")
        elif isinstance(event, ValueDownEvent):
            print(f"Aw shucks, {event.name}, went down from {event.old_value} to {event.new_value}")

class EmailNotifier(Observer):
    def update(self, event):
        if isinstance(event, ValueUpEvent):
            print(f"From @{event.name}: Went up from {event.old_value} to {event.new_value}")
        elif isinstance(event, ValueDownEvent):
            print(f"From @{event.name}: Went down from {event.old_value} to {event.new_value}")

class ProductObservers:
    def __init__(self):
        self.observers = []

    def attach_observers(self, *args:Observer):
        self.observers.extend(args)

    def detach_observers(self, *args:Observer):
        for observer in args:
            self.observers.remove(observer)

    def update_observers(self, event:Event):
        for observer in self.observers:
            observer.update(event=event)

#===============#
# PRODUCT CLASS #
#===============#
class Product:
    def __init__(self, name, value, observer_manager=None, event_factory=None):
        self.name = name
        self.old_value = None
        self.value = value
        # Dependency injection
        self.observer_manager = observer_manager or ProductObservers()
        self.event_factory = event_factory or EventFactory()
    
    def set_value(self, new_val):
        self.old_value = self.value
        self.value = new_val
        self.observer_manager.update_observers(self.event_factory.create_event(self.name, self.old_value, self.value))

if __name__ == "__main__":

    # Create products
    yak_razor = Product("Yak Razor", 0)

    # This will not notify any observers
    yak_razor.set_value(10)
    print(yak_razor.value)

    # Create observer
    sms = SMSNotifier()

    # Attach observer
    yak_razor.observer_manager.attach_observers(sms)
    yak_razor.set_value(10000)
    yak_razor.set_value(100)
