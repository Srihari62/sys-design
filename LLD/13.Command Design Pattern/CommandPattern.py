from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

# Receivers
class Light:
    def on(self) -> None:
        print("Light is ON")

    def off(self) -> None:
        print("Light is OFF")

class Fan:
    def on(self) -> None:
        print("Fan is ON")

    def off(self) -> None:
        print("Fan is OFF")

# Concrete Command for Light
class LightCommand(Command):
    def __init__(self, light: Light):
        self._light = light

    def execute(self) -> None:
        self._light.on()

    def undo(self) -> None:
        self._light.off()

# Concrete Command for Fan
class FanCommand(Command):
    def __init__(self, fan: Fan):
        self._fan = fan

    def execute(self) -> None:
        self._fan.on()

    def undo(self) -> None:
        self._fan.off()

# Invoker: Remote Controller with toggle behavior
class RemoteController:
    def __init__(self, num_buttons: int = 4):
        self._num_buttons = num_buttons
        self._buttons = [None] * num_buttons
        self._button_pressed = [False] * num_buttons

    def set_command(self, idx: int, cmd: Command) -> None:
        if 0 <= idx < self._num_buttons:
            self._buttons[idx] = cmd
            self._button_pressed[idx] = False

    def press_button(self, idx: int) -> None:
        if 0 <= idx < self._num_buttons and self._buttons[idx] is not None:
            if not self._button_pressed[idx]:
                self._buttons[idx].execute()
            else:
                self._buttons[idx].undo()
            self._button_pressed[idx] = not self._button_pressed[idx]
        else:
            print(f"No command assigned at button {idx}")

def main():
    # Receivers
    living_room_light = Light()
    ceiling_fan = Fan()

    # Invoker
    remote = RemoteController()

    # Setup Commands
    remote.set_command(0, LightCommand(living_room_light))
    remote.set_command(1, FanCommand(ceiling_fan))

    # Simulate button presses (toggle behavior)
    print("--- Toggling Light Button 0 ---")
    remote.press_button(0)  # ON
    remote.press_button(0)  # OFF

    print("--- Toggling Fan Button 1 ---")
    remote.press_button(1)  # ON
    remote.press_button(1)  # OFF

    # Press unassigned button to show default message
    print("--- Pressing Unassigned Button 2 ---")
    remote.press_button(2)

if __name__ == "__main__":
    main()
