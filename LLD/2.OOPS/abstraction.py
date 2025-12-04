from abc import ABC, abstractmethod

# ----------------------------------------------------------
# Abstract class --> 
# 1. Acts as an interface for the outside world to operate the car.
# 2. This abstract class defines 'WHAT' actions a Car can do,
#    rather than 'HOW' those actions are performed.
# 3. Since this is an abstract class, we cannot create objects of it directly.
# 4. Any class inheriting this MUST provide implementation for all abstract methods.
#
# 5. In real life, sitting inside a car you operate it using pedals/steering
#    without knowing the internal mechanism. Those controls are represented by this class.
# 6. 'Car' class represents the external interface (like pedals/buttons).
# ----------------------------------------------------------

class Car(ABC):

    @abstractmethod
    def startEngine(self):
        pass

    @abstractmethod
    def shiftGear(self, gear: int):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def stopEngine(self):
        pass


# ----------------------------------------------------------
# Concrete Class
# 1. This class provides implementation details for the abstract Car class.
# 2. Now we can create objects of 'SportsCar' and assign them to a 'Car' type reference.
#
# 3. In real life, this represents an actual car with internal mechanisms
#    for engine, gears, brakes, acceleration, etc.
#
# Therefore, we have two classes:
# - 'Car' → Interface / User controls (WHAT can be done)
# - 'SportsCar' → Actual functionality (HOW it works)
# ----------------------------------------------------------

class SportsCar(Car):

    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
        self.isEngineOn = False
        self.currentSpeed = 0
        self.currentGear = 0

    def startEngine(self):
        self.isEngineOn = True
        print(f"{self.brand} {self.model} : Engine starts with a roar!")

    def shiftGear(self, gear: int):
        if not self.isEngineOn:
            print(f"{self.brand} {self.model} : Engine is off! Cannot shift gear.")
            return
        self.currentGear = gear
        print(f"{self.brand} {self.model} : Shifted to gear {self.currentGear}")

    def accelerate(self):
        if not self.isEngineOn:
            print(f"{self.brand} {self.model} : Engine is off! Cannot accelerate.")
            return
        self.currentSpeed += 20
        print(f"{self.brand} {self.model} : Accelerating to {self.currentSpeed} km/h")

    def brake(self):
        self.currentSpeed -= 20
        if self.currentSpeed < 0:
            self.currentSpeed = 0
        print(f"{self.brand} {self.model} : Braking! Speed is now {self.currentSpeed} km/h")

    def stopEngine(self):
        self.isEngineOn = False
        self.currentGear = 0
        self.currentSpeed = 0
        print(f"{self.brand} {self.model} : Engine turned off.")


# ----------------------------------------------------------
# Main execution
# ----------------------------------------------------------
if __name__ == "__main__":
    # Creating a SportsCar object but referenced as a Car type (Polymorphism)
    myCar = SportsCar("Ford", "Mustang")

    # Using polymorphic behavior to operate the car
    myCar.startEngine()
    myCar.shiftGear(1)
    myCar.accelerate()
    myCar.shiftGear(2)
    myCar.accelerate()
    myCar.brake()
    myCar.stopEngine()
