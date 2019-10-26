
class Singleton:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    print(id(s1))
    print(id(s2))
    print(s1 is s2)
