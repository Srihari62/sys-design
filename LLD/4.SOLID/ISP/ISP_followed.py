# Separate interface for 2D shapes
class TwoDimensionalShape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


# Separate interface for 3D shapes
class ThreeDimensionalShape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def volume(self):
        raise NotImplementedError("Subclasses must implement volume()")


# Square implements only the 2D interface
class Square(TwoDimensionalShape):
    def __init__(self, s: float):
        self.side = s

    def area(self):
        return self.side * self.side


# Rectangle implements only the 2D interface
class Rectangle(TwoDimensionalShape):
    def __init__(self, l: float, w: float):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width


# Cube implements the 3D interface
class Cube(ThreeDimensionalShape):
    def __init__(self, s: float):
        self.side = s

    def area(self):
        return 6 * self.side * self.side

    def volume(self):
        return self.side * self.side * self.side


if __name__ == "__main__":
    square = Square(5)
    rectangle = Rectangle(4, 6)
    cube = Cube(3)

    print("Square Area:", square.area())
    print("Rectangle Area:", rectangle.area())
    print("Cube Area:", cube.area())
    print("Cube Volume:", cube.volume())
