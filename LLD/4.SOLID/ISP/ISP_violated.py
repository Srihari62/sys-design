# Single interface for all shapes (Violates ISP)
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def volume(self):
        raise NotImplementedError("Subclasses must implement volume()")  # 2D shapes don't have volume!


# Square is a 2D shape but is forced to implement volume()
class Square(Shape):
    def __init__(self, s: float):
        self.side = s

    def area(self):
        return self.side * self.side

    def volume(self):
        raise ValueError("Volume not applicable for Square")  # Unnecessary method


# Rectangle is also a 2D shape but is forced to implement volume()
class Rectangle(Shape):
    def __init__(self, l: float, w: float):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

    def volume(self):
        raise ValueError("Volume not applicable for Rectangle")  # Unnecessary method


# Cube is a 3D shape, so it actually has a volume
class Cube(Shape):
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

    try:
        print("Square Volume:", square.volume())  # Will throw an exception
    except ValueError as e:
        print("Exception:", e)
