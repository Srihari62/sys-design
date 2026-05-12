# Subsystems
class PowerSupply:
    def provide_power(self) -> None:
        print("Power Supply: Providing power...")

class CoolingSystem:
    def start_fans(self) -> None:
        print("Cooling System: Fans started...")

class CPU:
    def initialize(self) -> None:
        print("CPU: Initialization started...")

class Memory:
    def self_test(self) -> None:
        print("Memory: Self-test passed...")

class HardDrive:
    def spin_up(self) -> None:
        print("Hard Drive: Spinning up...")

class BIOS:
    def boot(self, cpu: CPU, memory: Memory) -> None:
        print("BIOS: Booting CPU and Memory checks...")
        cpu.initialize()
        memory.self_test()

class OperatingSystem:
    def load(self) -> None:
        print("Operating System: Loading into memory...")

# Facade
class ComputerFacade:
    def __init__(self):
        self._power_supply = PowerSupply()
        self._cooling_system = CoolingSystem()
        self._cpu = CPU()
        self._memory = Memory()
        self._hard_drive = HardDrive()
        self._bios = BIOS()
        self._os = OperatingSystem()

    def start_computer(self) -> None:
        print("----- Starting Computer -----")
        self._power_supply.provide_power()
        self._cooling_system.start_fans()
        self._bios.boot(self._cpu, self._memory)
        self._hard_drive.spin_up()
        self._os.load()
        print("Computer Booted Successfully!")

# Client
def main():
    computer = ComputerFacade()
    computer.start_computer()

if __name__ == "__main__":
    main()
