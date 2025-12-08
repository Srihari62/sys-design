# Class Invariant of a parent class Object should not be broken by child class Object.
# Hence child class can either maintain or strengthen the invariant but never narrow it down.

# Invariant: Balance cannot be negative
class BankAccount:
    def __init__(self, b: float):
        if b < 0:
            raise ValueError("Balance can't be negative")
        self.balance = b

    def withdraw(self, amount: float):
        if self.balance - amount < 0:
            raise RuntimeError("Insufficient funds")
        self.balance -= amount
        print(f"Amount withdrawn. Remaining balance is {self.balance}")


# Breaks invariant : Should not be allowed.
class CheatAccount(BankAccount):
    def __init__(self, b: float):
        super().__init__(b)

    def withdraw(self, amount: float):
        # LSP break! Negative balance allowed
        self.balance -= amount
        print(f"Amount withdrawn. Remaining balance is {self.balance}")


if __name__ == "__main__":
    bankAccount = BankAccount(100)
    bankAccount.withdraw(100)
