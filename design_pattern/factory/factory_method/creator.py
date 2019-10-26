from abc import ABC, abstractmethod

from factory.factory_method.product import Forward, Midfielder, Defender, Goalkeeper


class Formation(ABC):
    def __init__(self):
        self._line_up = []
        self.enroll_line_up()

    @abstractmethod
    def enroll_line_up(self):
        pass

    def set_player(self, player):
        self._line_up.append(player)

    def get_line_up(self):
        return self._line_up


class Liverpool(Formation):
    def enroll_line_up(self):
        self.set_player(Forward("Firmino"))
        self.set_player(Midfielder("Henderson"))
        self.set_player(Defender("Virgil"))
        self.set_player(Goalkeeper("Alison"))


class ManCity(Formation):
    def enroll_line_up(self):
        self.set_player(Forward("Aguero"))
        self.set_player(Midfielder("Kevin"))


if __name__ == "__main__":
    lfc = Liverpool()
    line_up = lfc.get_line_up()
    print(line_up)
