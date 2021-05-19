from abc import ABC, abstractmethod


class EventManager:
    def __init__(self):
        self.listeners = []

    def subscribe(self, listener):
        self.listeners.append(listener)

    def unsubscribe(self, listener):
        try:
            self.listeners.remove(listener)
        except ValueError:
            print("listener is not subscribed.")

    def notify(self, game, contents):
        for listener in self.listeners:
            listener.update(game, contents)


class Game:
    def __init__(self, name):
        self.name = name
        self.events = EventManager()

    def released(self):
        self.events.notify(self, "released")

    def discount(self):
        self.events.notify(self, "discount")


class Subscriber(ABC):
    @abstractmethod
    def update(self, game, contents):
        pass


class ConsoleSubscriber(Subscriber):
    def update(self, game, contents):
        print(f"Console: {game.name} {contents}")


class EmailSubscriber(Subscriber):
    def update(self, game, contents):
        print(f"Email: {game.name} {contents}")


g1 = Game("game1")
g2 = Game("game2")

email_subscriber = EmailSubscriber()
console_subscriber = ConsoleSubscriber()

g1.events.subscribe(email_subscriber)
g2.events.subscribe(email_subscriber)
g2.events.subscribe(console_subscriber)

g1.discount()
g2.released()