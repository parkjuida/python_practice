from abc import ABC, abstractmethod


class FootballPlayer(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def play(self):
        pass


class Forward(FootballPlayer):
    def __init__(self, name):
        super(Forward, self).__init__(name)

    def play(self):
        print("Attack")

    def train(self):
        print("Shooting")


class Midfielder(FootballPlayer):
    def __init__(self, name):
        super(Midfielder, self).__init__(name)

    def train(self):
        print("Pass")

    def play(self):
        print("Connect")


class Defender(FootballPlayer):
    def __init__(self, name):
        super(Defender, self).__init__(name)

    def train(self):
        print("Clearing")

    def play(self):
        print("Defend")


class Goalkeeper(FootballPlayer):
    def __init__(self, name):
        super(Goalkeeper, self).__init__(name)

    def train(self):
        print("Shoot defending")

    def play(self):
        print("Goal keeping")
