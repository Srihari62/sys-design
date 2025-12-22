from models.order import Order


class PickupOrder(Order):
    def __init__(self):
        super().__init__()
        self.restaurant_address = ""

    def get_type(self) -> str:
        return "Pickup"

    # Getters and Setters
    def set_restaurant_address(self, address: str):
        self.restaurant_address = address

    def get_restaurant_address(self) -> str:
        return self.restaurant_address
