# Return Type Rule :
# Subtype overridden method return type should be either identical
# or narrower than the parent method's return type.
# This is also called *return type covariance*.
# Python naturally supports covariance, as there is no strict return type enforcement.

class Animal:
    # some common Animal methods
    pass


class Dog(Animal):
    # Additional Dog methods specific to Dogs
    pass


class Parent:
    def getAnimal(self) -> Animal:
        print("Parent : Returning Animal instance")
        return Animal()


class Child(Parent):
    # Can also have return type as Dog (covariant return)
    def getAnimal(self) -> Animal:
        print("Child : Returning Dog instance")
        return Dog()


class Client:
    def __init__(self, p: Parent):
        self.p = p

    def takeAnimal(self):
        self.p.getAnimal()


if __name__ == "__main__":
    
    parent = Parent()
    child = Child()

    client = Client(child)
    # client = Client(parent)

    client.takeAnimal()
