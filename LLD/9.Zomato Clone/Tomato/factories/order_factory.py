from abc import ABC, abstractmethod


class OrderFactory(ABC):
    @abstractmethod
    def create_order(
        self,
        user,
        cart,
        restaurant,
        menu_items,
        payment_strategy,
        total_cost: float,
        order_type: str,
    ):
        pass
