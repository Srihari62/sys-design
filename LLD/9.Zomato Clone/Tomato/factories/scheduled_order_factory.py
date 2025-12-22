from factories.order_factory import OrderFactory
from models.delivery_order import DeliveryOrder
from models.pickup_order import PickupOrder


class ScheduledOrderFactory(OrderFactory):
    def __init__(self, schedule_time: str):
        self.schedule_time = schedule_time

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
        order = None

        if order_type == "Delivery":
            delivery_order = DeliveryOrder()
            delivery_order.set_user_address(user.get_address())
            order = delivery_order
        else:
            pickup_order = PickupOrder()
            pickup_order.set_restaurant_address(restaurant.get_location())
            order = pickup_order

        order.set_user(user)
        order.set_restaurant(restaurant)
        order.set_items(menu_items)
        order.set_payment_strategy(payment_strategy)
        order.set_scheduled(self.schedule_time)
        order.set_total(total_cost)

        return order
