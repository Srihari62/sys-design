from models.cart import Cart

class User:
    def __init__(self, user_id: int, name: str, address: str):
        self.user_id = user_id
        self.name = name
        self.address = address
        self.cart = Cart()

    # Getters and Setters
    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_address(self) -> str:
        return self.address

    def set_address(self, address: str):
        self.address = address

    def get_cart(self) -> Cart:
        return self.cart
