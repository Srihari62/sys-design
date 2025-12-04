from abc import ABC, abstractmethod

"""
We know that real world Objects show inheritance relationship where we
have parent object and child object. Child object has all the characters
or behaviours that parent have plus some additional characters/behaviours.

Like all cars in real world have a brand, model etc and can start, stop,
accelerate etc. But some specific cars like Manual cars have gear system
while other specific cars like Electric cars have battery system.

We represent this scenario of real world in programming by creating a parent class
and defining all the characters (variables) and behaviours (methods) that
all cars have in parent class. Then we create different child classes that
inherit from this parent class and define only those characters and behaviours
that are specific to them. Although objects of these child classes can
access or call parent class characters (variables) and behaviours (methods).
Hence providing code reusability.
"""

class Car(ABC):  # Parent class representing Generic Car
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_engine_on = False
        self.current_speed = 0

    # Common methods for ALL cars
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    # Generic accelerate behaviour (same for all cars)
    def accelerate(self):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Cannot accelerate! Engine is off.")
            return
        self.current_speed += 20
        print(f"{self.brand} {self.model} : Accelerating to {self.current_speed} km/h")

    # Generic brake behaviour (same for all cars)
    def brake(self):
        self.current_speed -= 20
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.brand} {self.model} : Braking! Speed is now {self.current_speed} km/h")


class ManualCar(Car):  # Child class - Inherits from Car
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.current_gear = 0  # Specific to Manual Cars

    # Specialized method for Manual Car
    def shift_gear(self, gear):
        self.current_gear = gear
        print(f"{self.brand} {self.model} : Shifted to gear {self.current_gear}")

    # Overriding abstract methods
    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.brand} {self.model} : Manual engine started.")

    def stop_engine(self):
        self.is_engine_on = False
        self.current_speed = 0
        print(f"{self.brand} {self.model} : Manual engine turned off.")


class ElectricCar(Car):  # Child class - Inherits from Car
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.battery_level = 100  # Specific to Electric Cars

    # Specialized method for Electric Car
    def charge_battery(self):
        self.battery_level = 100
        print(f"{self.brand} {self.model} : Battery fully charged!")

    # Overriding abstract methods
    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.brand} {self.model} : Electric motor powered on.")

    def stop_engine(self):
        self.is_engine_on = False
        self.current_speed = 0
        print(f"{self.brand} {self.model} : Electric motor turned off.")


# Main Method
if __name__ == "__main__":
    myManualCar = ManualCar("Suzuki", "WagonR")
    myManualCar.start_engine()
    myManualCar.shift_gear(1)  # Specific to Manual Car
    myManualCar.accelerate()
    myManualCar.brake()
    myManualCar.stop_engine()

    print("----------------------")

    myElectricCar = ElectricCar("Tesla", "Model S")
    myElectricCar.charge_battery()  # Specific to Electric Car
    myElectricCar.start_engine()
    myElectricCar.accelerate()
    myElectricCar.brake()
    myElectricCar.stop_engine()
