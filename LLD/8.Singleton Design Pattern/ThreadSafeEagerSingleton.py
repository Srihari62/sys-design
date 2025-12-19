class Singleton:
    # Eagerly created instance (static initialization)
    _instance = None

    def __init__(self):
        print("Singleton Constructor Called!")

    @classmethod
    def get_instance(cls):
        return cls._instance


# Eager initialization (happens at class load time)
Singleton._instance = Singleton()


if __name__ == "__main__":
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()

    # Identity comparison (same as pointer comparison in C++)
    print(s1 is s2)
