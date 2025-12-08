# Method Argument Rule : 
# Subtype method arguments can be identical or wider than the supertype
# Python allows flexible method overriding since parameters aren't typed strictly like C++

class Parent:
    def print(self, msg: str):
        print("Parent:", msg)


class Child(Parent):
    def print(self, msg: str):  # override allowed
        print("Child:", msg)


# Client that pass string as msg as client expects.
class Client:
    def __init__(self, p: Parent):
        self.p = p

    def printMsg(self):
        self.p.print("Hello")


if __name__ == "__main__":

        parent = Parent()
        child = Child()

        # client = Client(parent)
        client = Client(child)

        client.printMsg()
