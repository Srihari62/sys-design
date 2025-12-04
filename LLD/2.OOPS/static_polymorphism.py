"""
Static Polymorphism (Compile-time polymorphism) in real life says that
the same action can behave differently depending on the input parameters.
For example, a Manual car can accelerate by a fixed amount or by a
specific amount you request. In programming, we achieve this via method
overloading: multiple methods with the same name but different signatures.
"""

class ManualCar:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_engine_on = False
        self.current_speed = 0
        self.current_gear = 0

    def start_engine(self):
        self.is_engine_on = True
        print(f"{self.brand} {self.model} : Engine started.")

    def stop_engine(self):
        self.is_engine_on = False
        self.current_speed = 0
        print(f"{self.brand} {self.model} : Engine turned off.")

    # Simulating Method Overloading using Default Argument
    def accelerate(self, speed=None):
        if not self.is_engine_on:
            print(f"{self.brand} {self.model} : Cannot accelerate! Engine is off.")
            return
        
        if speed is None:
            speed = 20  # Default speed
        
        self.current_speed += speed
        print(f"{self.brand} {self.model} : Accelerating to {self.current_speed} km/h")

    def brake(self):
        self.current_speed -= 20
        if self.current_speed < 0:
            self.current_speed = 0
        print(f"{self.brand} {self.model} : Braking! Speed is now {self.current_speed} km/h")

    def shift_gear(self, gear):
        self.current_gear = gear
        print(f"{self.brand} {self.model} : Shifted to gear {self.current_gear}")


# Main function
if __name__ == "__main__":
    myManualCar = ManualCar("Suzuki", "WagonR")
    myManualCar.start_engine()
    myManualCar.accelerate()      # Uses default +20 km/h
    myManualCar.accelerate(40)    # Uses custom speed
    myManualCar.brake()
    myManualCar.stop_engine()
