from abc import ABC, abstractmethod

class IDataService(ABC):
    @abstractmethod
    def fetch_data(self) -> str:
        pass

class RealDataService(IDataService):
    def __init__(self):
        # Imagine this connects to a remote server or loads heavy resources.
        print("[RealDataService] Initialized (simulating remote setup)")

    def fetch_data(self) -> str:
        return "[RealDataService] Data from server"

# Remote proxy
class DataServiceProxy(IDataService):
    def __init__(self):
        self._real_service = RealDataService()

    def fetch_data(self) -> str:
        print("[DataServiceProxy] Connecting to remote service...")
        return self._real_service.fetch_data()

def main():
    data_service = DataServiceProxy()
    print(data_service.fetch_data())

if __name__ == "__main__":
    main()
