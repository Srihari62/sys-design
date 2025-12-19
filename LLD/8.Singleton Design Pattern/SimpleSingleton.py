class Singleton:
    _instance = None   # static class variable

    def __init__(self):
        print("Singleton Constructor called")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


if __name__ == "__main__":
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()

    # Identity comparison (same as pointer comparison in C++)
    print(s1 is s2)
