import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()   # static mutex

    def __init__(self):
        print("Singleton Constructor Called!")

    @classmethod
    def get_instance(cls):
        # First check (no locking)
        if cls._instance is None:
            with cls._lock:   # lock only if needed
                # Second check (after acquiring lock)
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance


if __name__ == "__main__":
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()

    # Identity comparison (same as pointer comparison in C++)
    print(s1 is s2)
