class Singleton:

    def __init__(self, target_class):
        self._target_class = target_class

    def __call__(self, *args, **kwargs):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._target_class()
            return self._instance


if __name__ == "__main__":
    @Singleton
    class A:
        pass


    @Singleton
    class B:
        pass


    a1 = A()
    a2 = A()
    print(id(a1))
    print(id(a2))
    print(a1 is a2)

    b1 = B()
    b2 = B()
    print(id(b1))
    print(id(b2))
    print(b1 is b2)
    