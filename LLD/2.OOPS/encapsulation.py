# ----------------------------------------------------------
# Encapsulation says 2 things:
# 1. An Object's characteristics and behaviors are encapsulated together
#    within that object.
# 2. Not everything should be accessible to everyone.
#    Object should provide data security.
#
# We implement Encapsulation in Python by:
# 1. Creating a class that contains attributes and methods together.
# 2. Making some attributes private using "__" (name mangling)
#    and exposing them safely using getters & setters.
# ----------------------------------------------------------

class SportsCar:

    def __init__(self, brand: str, model: str):
        # Private attributes using double underscore (__)
        self.__brand = brand
        self.__model = model
        self.__isEngineOn = False
        self.__currentSpeed = 0
        self.__currentGear = 0
        
        # New private variable for explaining setters
        self.__tyreCompany = "MRF"

    # Getter method for Speed
    def getSpeed(self):
        return self.__currentSpeed

    # Getter for Tyre Company
    def getTyreCompany(self):
        return self.__tyreCompany

    # Setter for Tyre Company
    def setTyreCompany(self, tyreCompany: str):
        self.__tyreCompany = tyreCompany

    def startEngine(self):
        self.__isEngineOn = True
        print(f"{self.__brand} {self.__model} : Engine starts with a roar!")

    def shiftGear(self, gear: int):
        if not self.__isEngineOn:
            print(f"{self.__brand} {self.__model} : Engine is off! Cannot Shift Gear.")
            return
        self.__currentGear = gear
        print(f"{self.__brand} {self.__model} : Shifted to gear {self.__currentGear}")

    def accelerate(self):
        if not self.__isEngineOn:
            print(f"{self.__brand} {self.__model} : Engine is off! Cannot accelerate.")
            return
        self.__currentSpeed += 20
        print(f"{self.__brand} {self.__model} : Accelerating to {self.__currentSpeed} km/h")

    def brake(self):
        self.__currentSpeed -= 20
        if self.__currentSpeed < 0:
            self.__currentSpeed = 0
        print(f"{self.__brand} {self.__model} : Braking! Speed is now {self.__currentSpeed} km/h")

    def stopEngine(self):
        self.__isEngineOn = False
        self.__currentGear = 0
        self.__currentSpeed = 0
        print(f"{self.__brand} {self.__model} : Engine turned off.")

# ----------------------------------------------------------
# Main Execution
# ----------------------------------------------------------
if __name__ == "__main__":
    
    mySportsCar = SportsCar("Ford", "Mustang")

    mySportsCar.startEngine()
    mySportsCar.shiftGear(1)
    mySportsCar.accelerate()
    mySportsCar.shiftGear(2)
    mySportsCar.accelerate()
    mySportsCar.brake()
    mySportsCar.stopEngine()

    # ❌ Direct access to private variable will fail:
    # mySportsCar.__currentSpeed = 500  # Attribute Error, encapsulated

    # ✔ Proper way: Using getter method
    print("Current Speed of My Sports Car is", mySportsCar.getSpeed())
