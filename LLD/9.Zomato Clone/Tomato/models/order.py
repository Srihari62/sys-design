from abc import ABC, abstractmethod

class Order(ABC):
    next_order_id = 0

    def __init__(self):
        self.user = None
        self.restaurant = None
        self.items = []
        self.payment_strategy = None
        self.total = 0.0
        self.scheduled = ""
        Order.next_order_id += 1
        self.order_id = Order.next_order_id

    def process_payment(self) -> bool:
        if self.payment_strategy:
            self.payment_strategy.pay(self.total)
            return True
        else:
            print("Please choose a payment mode first")
            return False

    @abstractmethod
    def get_type(self) -> str:
        pass

    # Getters and Setters
    def get_order_id(self) -> int:
        return self.order_id

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user

    def set_restaurant(self, restaurant):
        self.restaurant = restaurant

    def get_restaurant(self):
        return self.restaurant

    def set_items(self, items: list):
        self.items = items
        self.total = sum(item.get_price() for item in items)

    def get_items(self) -> list:
        return self.items

    def set_payment_strategy(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def set_scheduled(self, scheduled: str):
        self.scheduled = scheduled

    def get_scheduled(self) -> str:
        return self.scheduled

    def get_total(self) -> float:
        return self.total

    def set_total(self, total: float):
        self.total = total
