from abc import ABC, abstractmethod
from typing import Optional

# Abstract Handler (Base Class)
class MoneyHandler(ABC):
    def __init__(self):
        self._next_handler: Optional[MoneyHandler] = None

    def set_next_handler(self, next_handler: 'MoneyHandler'):
        self._next_handler = next_handler

    @abstractmethod
    def dispense(self, amount: int):
        pass


class BaseNoteHandler(MoneyHandler):
    """Refactored common logic into a base class to avoid duplication"""
    def __init__(self, denomination: int, num_notes: int):
        super().__init__()
        self._denomination = denomination
        self._num_notes = num_notes

    def dispense(self, amount: int):
        notes_needed = amount // self._denomination

        if notes_needed > self._num_notes:
            notes_needed = self._num_notes
            self._num_notes = 0
        else:
            self._num_notes -= notes_needed

        if notes_needed > 0:
            print(f"Dispensing {notes_needed} x ₹{self._denomination} notes.")

        remaining_amount = amount - (notes_needed * self._denomination)
        
        if remaining_amount > 0:
            if self._next_handler is not None:
                self._next_handler.dispense(remaining_amount)
            else:
                print(f"Remaining amount of ₹{remaining_amount} cannot be fulfilled (Insufficient funds in ATM)")


# Concrete Handlers
class ThousandHandler(BaseNoteHandler):
    def __init__(self, num_notes: int):
        super().__init__(1000, num_notes)

class FiveHundredHandler(BaseNoteHandler):
    def __init__(self, num_notes: int):
        super().__init__(500, num_notes)

class TwoHundredHandler(BaseNoteHandler):
    def __init__(self, num_notes: int):
        super().__init__(200, num_notes)

class HundredHandler(BaseNoteHandler):
    def __init__(self, num_notes: int):
        super().__init__(100, num_notes)


# Client Code
def main():
    # Creating handlers for each note type
    thousand_handler = ThousandHandler(3)
    five_hundred_handler = FiveHundredHandler(5)
    two_hundred_handler = TwoHundredHandler(10)
    hundred_handler = HundredHandler(20)

    # Setting up the chain of responsibility
    thousand_handler.set_next_handler(five_hundred_handler)
    five_hundred_handler.set_next_handler(two_hundred_handler)
    two_hundred_handler.set_next_handler(hundred_handler)

    amount_to_withdraw = 4000

    # Initiating the chain
    print(f"\nDispensing amount: ₹{amount_to_withdraw}")
    thousand_handler.dispense(amount_to_withdraw)

if __name__ == "__main__":
    main()
