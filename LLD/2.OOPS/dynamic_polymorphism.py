from abc import ABC, abstractmethod

# ------------------------------------------------------------
# Dynamic Polymorphism real life: 
# A Manual Car and Electric Car both respond to accelerate()
# but respond differently.
#
# Parent class Car defines common features but keeps behavior
# abstract where child classes provide their own implementation.
# ------------------------------------------------------------

class Car(ABC):
    def __init__(self, brand: str, model: str):
        self._brand = brand
        self._model = model
        self._isEngineOn = False
        self._currentSpeed = 0

    # Common methods to all Cars
    def startEngine(self):
        self._isEngineOn = True
        print(f"{self._brand} {self._model} : Engine started.")

    def stopEngine(self):
        self._isEngineOn = False
        self._currentSpeed = 0
        print(f"{self._brand} {self._model} : Engine turned off.")

    # Abstract methods used for Dynamic Polymorphism
    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def brake(self):
        pass


# ------------------------------------------------------------
# Manual Car Implementation
# ------------------------------------------------------------
class ManualCar(Car):
    def __init__(self, brand: str, model: str):
        super().__init__(brand, model)
        self._currentGear = 0

    def shiftGear(self, gear: int):
        self._currentGear = gear
        print(f"{self._brand} {self._model} : Shifted to gear {self._currentGear}")

    # Overriding accelerate method
    def accelerate(self):
        if not self._isEngineOn:
            print(f"{self._brand} {self._model} : Cannot accelerate! Engine is off.")
            return
        self._currentSpeed += 20
        print(f"{self._brand} {self._model} : Accelerating to {self._currentSpeed} km/h")

    # Overriding brake method
    def brake(self):
        self._currentSpeed -= 20
        if self._currentSpeed < 0:
            self._currentSpeed = 0
        print(f"{self._brand} {self._model} : Braking! Speed is now {self._currentSpeed} km/h")


# ------------------------------------------------------------
# Electric Car Implementation
# ------------------------------------------------------------
class ElectricCar(Car):
    def __init__(self, brand: str, model: str):
        super().__init__(brand, model)
        self._batteryLevel = 100

    def chargeBattery(self):
        self._batteryLevel = 100
        print(f"{self._brand} {self._model} : Battery fully charged!")

    # Overriding accelerate method
    def accelerate(self):
        if not self._isEngineOn:
            print(f"{self._brand} {self._model} : Cannot accelerate! Engine is off.")
            return
        if self._batteryLevel <= 0:
            print(f"{self._brand} {self._model} : Battery dead! Cannot accelerate.")
            return
        self._batteryLevel -= 10
        self._currentSpeed += 15
        print(f"{self._brand} {self._model} : Accelerating to {self._currentSpeed} km/h. Battery at {self._batteryLevel}%.")

    # Overriding brake method
    def brake(self):
        self._currentSpeed -= 15
        if self._currentSpeed < 0:
            self._currentSpeed = 0
        print(f"{self._brand} {self._model} : Regenerative braking! Speed is now {self._currentSpeed} km/h. Battery at {self._batteryLevel}%.")


# ------------------------------------------------------------
# Main Execution - Demonstrates Dynamic Polymorphism
# ------------------------------------------------------------
if __name__ == "__main__":
    myManualCar = ManualCar("Suzuki", "WagonR")
    myManualCar.startEngine()
    myManualCar.accelerate()
    myManualCar.accelerate()
    myManualCar.brake()
    myManualCar.stopEngine()

    print("----------------------")

    myElectricCar = ElectricCar("Tesla", "Model S")
    myElectricCar.startEngine()
    myElectricCar.accelerate()
    myElectricCar.accelerate()
    myElectricCar.brake()
    myElectricCar.stopEngine()
