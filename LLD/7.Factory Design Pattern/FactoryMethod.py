from abc import ABC, abstractmethod

# ---------------- Product Class ----------------
class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass


class BasicBurger(Burger):
    def prepare(self):
        print("Preparing Basic Burger with bun, patty, and ketchup!")


class StandardBurger(Burger):
    def prepare(self):
        print("Preparing Standard Burger with bun, patty, cheese, and lettuce!")


class PremiumBurger(Burger):
    def prepare(self):
        print("Preparing Premium Burger with gourmet bun, premium patty, cheese, lettuce, and secret sauce!")


class BasicWheatBurger(Burger):
    def prepare(self):
        print("Preparing Basic Wheat Burger with bun, patty, and ketchup!")


class StandardWheatBurger(Burger):
    def prepare(self):
        print("Preparing Standard Wheat Burger with bun, patty, cheese, and lettuce!")


class PremiumWheatBurger(Burger):
    def prepare(self):
        print("Preparing Premium Wheat Burger with gourmet bun, premium patty, cheese, lettuce, and secret sauce!")


# ---------------- Factory ----------------
class BurgerFactory(ABC):
    @abstractmethod
    def create_burger(self, type):
        pass


class SinghBurger(BurgerFactory):
    def create_burger(self, type):
        if type == "basic":
            return BasicBurger()
        elif type == "standard":
            return StandardBurger()
        elif type == "premium":
            return PremiumBurger()
        else:
            print("Invalid burger type!")
            return None


class KingBurger(BurgerFactory):
    def create_burger(self, type):
        if type == "basic":
            return BasicWheatBurger()
        elif type == "standard":
            return StandardWheatBurger()
        elif type == "premium":
            return PremiumWheatBurger()
        else:
            print("Invalid burger type!")
            return None


# ---------------- Client Code ----------------
if __name__ == "__main__":
    burger_type = "basic"

    my_factory = SinghBurger()

    burger = my_factory.create_burger(burger_type)

    if burger:
        burger.prepare()
