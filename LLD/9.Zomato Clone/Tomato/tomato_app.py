from models.user import User
from models.restaurant import Restaurant
from models.menu_item import MenuItem
from models.cart import Cart
from managers.restaurant_manager import RestaurantManager
from managers.order_manager import OrderManager
from strategies.payment_strategy import PaymentStrategy
from strategies.upi_payment_strategy import UpiPaymentStrategy
from factories.now_order_factory import NowOrderFactory
from factories.scheduled_order_factory import ScheduledOrderFactory
from services.notification_service import NotificationService

class TomatoApp:
    def __init__(self):
        self.initialize_restaurants()

    def initialize_restaurants(self):
        # Sample Restaurant 1
        restaurant1 = Restaurant("Bikaner", "Delhi")
        restaurant1.add_menu_item(MenuItem("P1", "Chole Bhature", 120))
        restaurant1.add_menu_item(MenuItem("P2", "Samosa", 15))

        # Sample Restaurant 2
        restaurant2 = Restaurant("Haldiram", "Kolkata")
        restaurant2.add_menu_item(MenuItem("P1", "Raj Kachori", 80))
        restaurant2.add_menu_item(MenuItem("P2", "Pav Bhaji", 100))
        restaurant2.add_menu_item(MenuItem("P3", "Dhokla", 50))

        # Sample Restaurant 3
        restaurant3 = Restaurant("Saravana Bhavan", "Chennai")
        restaurant3.add_menu_item(MenuItem("P1", "Masala Dosa", 90))
        restaurant3.add_menu_item(MenuItem("P2", "Idli Vada", 60))
        restaurant3.add_menu_item(MenuItem("P3", "Filter Coffee", 30))

        # Register restaurants
        restaurant_manager = RestaurantManager.get_instance()
        restaurant_manager.add_restaurant(restaurant1)
        restaurant_manager.add_restaurant(restaurant2)
        restaurant_manager.add_restaurant(restaurant3)

    def search_restaurants(self, location: str):
        return RestaurantManager.get_instance().search_by_location(location)

    def select_restaurant(self, user: User, restaurant: Restaurant):
        cart = user.get_cart()
        cart.set_restaurant(restaurant)

    def add_to_cart(self, user: User, item_code: str):
        restaurant = user.get_cart().get_restaurant()
        if not restaurant:
            print("Please select a restaurant first.")
            return
        for item in restaurant.get_menu():
            if item.get_code() == item_code:
                user.get_cart().add_item(item)
                break

    def checkout_now(self, user: User, order_type: str, payment_strategy: PaymentStrategy):
        return self.checkout(user, order_type, payment_strategy, NowOrderFactory())

    def checkout_scheduled(self, user: User, order_type: str, payment_strategy: PaymentStrategy, schedule_time: str):
        return self.checkout(user, order_type, payment_strategy, ScheduledOrderFactory(schedule_time))

    def checkout(self, user: User, order_type: str, payment_strategy: PaymentStrategy, order_factory):
        if user.get_cart().is_empty():
            return None

        user_cart = user.get_cart()
        ordered_restaurant = user_cart.get_restaurant()
        items_ordered = user_cart.get_items()
        total_cost = user_cart.get_total_cost()

        order = order_factory.create_order(user, user_cart, ordered_restaurant, items_ordered, payment_strategy, total_cost, order_type)
        OrderManager.get_instance().add_order(order)
        return order

    def pay_for_order(self, user: User, order):
        is_payment_success = order.process_payment()
        if is_payment_success:
            notification = NotificationService()
            notification.notify(order)
            user.get_cart().clear()

    def print_user_cart(self, user: User):
        print("Items in cart:")
        print("------------------------------------")
        for item in user.get_cart().get_items():
            print(f"{item.get_code()} : {item.get_name()} : ₹{item.get_price()}")
        print("------------------------------------")
        print(f"Grand total : ₹{user.get_cart().get_total_cost()}")
