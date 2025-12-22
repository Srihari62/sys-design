class RestaurantManager:
    _instance = None

    def __init__(self):
        if RestaurantManager._instance is not None:
            raise Exception("This class is a singleton!")
        self.restaurants = []

    @staticmethod
    def get_instance():
        if RestaurantManager._instance is None:
            RestaurantManager._instance = RestaurantManager()
        return RestaurantManager._instance

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def search_by_location(self, location: str):
        location = location.lower()
        result = []

        for restaurant in self.restaurants:
            if restaurant.get_location().lower() == location:
                result.append(restaurant)

        return result
