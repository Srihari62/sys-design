from abc import ABC, abstractmethod

# Base Car class
class Car(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_engine_on = False
        self.current_speed = 0

    # Common methods for ALL cars
    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.brand} {self.model} : Engine started.")

    def stop_engine(self):
        self.is_engine_on = False
        self.current_speed = 0
        print(f"{self.brand} {self.model} : Engine turned off.")

    @abstractmethod
    def accelerate(self, speed=None):  
        """
        Abstract method for both:
        - Dynamic Polymorphism (no args)
        - Static-like Polymorphism (speed arg)
        In Python we simulate both in one method using default parameter.
        """
        pass

    @abstractmethod
    def brake(self):  # Abstract method for Dynamic Polymorphism
        pass


class ManualCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.current_gear = 0

    # Specialized method for Manual Car
    def shift_gear(self, gear):
        self.current_gear = gear
        print(f"{self.brand} {self.model} : Shifted to gear {self.current_gear}")

    # Overriding + Overloading accelerate simulation
    def accelerate(self, speed=None):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Cannot accelerate! Engine is off.")
            return

        if speed is None:
            speed = 20  # Default speed like C++ version

        self.current_speed += speed
        print(f"{self.brand} {self.model} : Accelerating to {self.current_speed} km/h")

    # Overriding brake - Dynamic Polymorphism
    def brake(self):
        self.current_speed -= 20
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.brand} {self.model} : Braking! Speed is now {self.current_speed} km/h")


class ElectricCar(Car):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.battery_level = 100

    # Specialized method for Electric Car
    def charge_battery(self):
        self.battery_level = 100
        print(f"{self.brand} {self.model} : Battery fully charged!")

    # Overriding accelerate - Dynamic + Static Polymorphism simulation
    def accelerate(self, speed=None):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Cannot accelerate! Engine is off.")
            return

        if self.battery_level <= 0:
            print(f"{self.brand} {self.model} : Battery dead! Cannot accelerate.")
            return

        if speed is None:
            speed = 15

        self.current_speed += speed
        self.battery_level -= (10 + speed)
        print(f"{self.brand} {self.model} : Accelerating to {self.current_speed} km/h. Battery at {self.battery_level}%.")

    # Overriding brake - Dynamic Polymorphism
    def brake(self):
        self.current_speed -= 15
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.brand} {self.model} : Regenerative braking! Speed is now {self.current_speed} km/h. Battery at {self.battery_level}%.")


# Main function
if __name__ == "__main__":
    myManualCar = ManualCar("Ford", "Mustang")
    myManualCar.start_engine()
    myManualCar.accelerate()
    myManualCar.accelerate()
    myManualCar.brake()
    myManualCar.stop_engine()

    print("----------------------")

    myElectricCar = ElectricCar("Tesla", "Model S")
    myElectricCar.start_engine()
    myElectricCar.accelerate()
    myElectricCar.accelerate()
    myElectricCar.brake()
    myElectricCar.stop_engine()
