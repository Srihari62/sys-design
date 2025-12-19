import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()   # static mutex

    def __init__(self):
        print("Singleton Constructor Called!")

    @classmethod
    def get_instance(cls):
        # Lock every time (simple & safe)
        with cls._lock:
            if cls._instance is None:
                cls._instance = cls()
        return cls._instance


if __name__ == "__main__":
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()

    # Identity comparison (same as pointer comparison in C++)
    print(s1 is s2)
