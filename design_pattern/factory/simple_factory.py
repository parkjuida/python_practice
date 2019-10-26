from abc import ABC, abstractmethod


class FootballClub(ABC):
    @abstractmethod
    def get_stadium_name(self):
        pass


class LiverpoolFC(FootballClub):
    def get_stadium_name(self):
        return "Ann Field"


class ManchesterCity(FootballClub):
    def get_stadium_name(self):
        return "Etihad Stadium"


class FootballClubFactory:
    @staticmethod
    def get_football_club(name: str) -> FootballClub:
        return eval(name)()

    @staticmethod
    def get_home_stadium_name(name: str) -> str:
        return eval(name)().get_stadium_name()


if __name__ == "__main__":
    fcf = FootballClubFactory()
    liverpool = fcf.get_football_club("LiverpoolFC")
    mcfc = fcf.get_football_club("ManchesterCity")
    a = liverpool.get_stadium_name()
    b = mcfc.get_stadium_name()
    c = fcf.get_home_stadium_name("LiverpoolFC")
    print(a, b, c)
