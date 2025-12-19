from abc import ABC, abstractmethod

# ---------------- Product ----------------
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


# ---------------- Factory ----------------
class BurgerFactory:
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


# ---------------- Client Code ----------------
if __name__ == "__main__":
    burger_type = "standard"

    my_burger_factory = BurgerFactory()

    burger = my_burger_factory.create_burger(burger_type)

    if burger:
        burger.prepare()
