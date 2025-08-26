
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Print(Command):
    def __init__(self, reciever, contents:str):
        self.contents = contents
        self.reciever = reciever

    def execute(self):
        self.reciever.print_out(self.contents)
    
class Reciever:
    def print_out(self, contents:str):
        "Complex business logic goes in here"

        if contents[-1] == ".":
            contents = contents[:-1]
        contents += "..."

        print(contents)

class Invoker:
    def command(self, cmd:Command):
        self.command = cmd
    
    def execute(self):
        self.command.execute()

if __name__ == "__main__":

    printer = Reciever()
    print_out = Print(printer, 
                      "Dear Basketball, " \
                      "Ever since I started rolling up my dad's tube socks, and shooting imaginary hoops yada yada yada.")
    invoker = Invoker()

    invoker.command(print_out)
    invoker.execute()

    