
from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, reciever, contents):
        self.reciever = reciever
        self.contents = contents

    @abstractmethod
    def execute(self):
        "Give a command to a reciever to apply business logic and execute"

class Print(Command):
    def execute(self):
        self.reciever.print_out(self.contents)

class Fax(Command):
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
    def __init__(self):
        self.queue = []
    
    def register(self, *args: Command):
        self.queue.extend(args)
    
    def execute(self, cmd: Command):
        cmd.execute()
    
    def execute_all(self):
        for cmd in self.queue:
            cmd.execute()
        self.queue.clear()

if __name__ == "__main__":

    # Create a reciever, printer; a command, print out; and an invoker
    printer = Reciever()
    print_out = Print(printer, 
                      "Dear Basketball, " \
                      "Ever since I started rolling up my dad's tube socks, and shooting imaginary hoops yada yada yada.")
    
    invoker = Invoker()

    # Execute the print out command
    invoker.execute(print_out)

    # Create a new command
    fax = Fax(printer,
              "HOW DOES FAXING WORK <|*_*|>")
    
    # Register the commands and execute them all
    invoker.register(fax)
    invoker.register(print_out)

    invoker.execute_all()

    