class MenuItem:
    def __init__(self, code: str, name: str, price: int):
        self.code = code
        self.name = name
        self.price = price

    # Getters and setters
    def get_code(self) -> str:
        return self.code

    def set_code(self, code: str):
        self.code = code

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_price(self) -> int:
        return self.price

    def set_price(self, price: int):
        self.price = price
