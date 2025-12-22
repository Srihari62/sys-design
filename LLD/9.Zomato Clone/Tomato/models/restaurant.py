from models.menu_item import MenuItem

class Restaurant:
    next_restaurant_id = 0

    def __init__(self, name: str, location: str):
        self.name = name
        self.location = location
        Restaurant.next_restaurant_id += 1
        self.restaurant_id = Restaurant.next_restaurant_id
        self.menu = []

    # Getters and Setters
    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_location(self) -> str:
        return self.location

    def set_location(self, location: str):
        self.location = location

    def add_menu_item(self, item: MenuItem):
        self.menu.append(item)

    def get_menu(self) -> list:
        return self.menu

    # Optional: destructor behavior (Python GC handles this)
    # def __del__(self):
    #     print(f"Destroying Restaurant: {self.name}, and clearing its menu.")
    #     self.menu.clear()
