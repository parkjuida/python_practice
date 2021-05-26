from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver
        self.argument = "Command A"

    def execute(self):
        self.receiver.action(self.argument)


class Receiver:
    def action(self, arg):
        print(f"I`m receiver {arg}")


class Invoker:
    def invoke(self, cmd):
        cmd.execute()


r = Receiver()
c = ConcreteCommand(r)
invoker = Invoker()
invoker.invoke(c)