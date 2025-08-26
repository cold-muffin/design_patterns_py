
from random import shuffle
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def organize(self, lst:list):
        "Organizes a list based on a strategy"

class LeastToGreatest(Strategy):
    def organize(self, lst):
        lst.sort()
        return lst

class GreatestToLeast(Strategy):
    def organize(self, lst):
        lst.sort(reverse=True)
        return lst
    
class Randomize(Strategy):
    def organize(self, lst):
        shuffle(lst)
        return lst

class Database:
    def __init__(self, lst):
        self.data = lst

    def organize(self, strat:Strategy):
        old_data = self.data
        self.data = strat.organize(self.data)
        print(f"{old_data} -> {self.data}")

if __name__ == "__main__":

    # Create strategy objects
    ltg = LeastToGreatest()
    gtl = GreatestToLeast()
    rndm = Randomize()

    # Create database
    db = Database([1, 524, 5, 2, 35, 235, 0, 5])

    # Implemenet strategies
    db.organize(ltg)
    db.organize(rndm)
    db.organize(gtl)