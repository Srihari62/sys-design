# Sub class methods should not allow state changes that
# Base class never allowed.

class BankAccount:
    def __init__(self, b: float):
        if b < 0:
            raise ValueError("Balance can't be negative")
        self.balance = b

    # History Constraint : Withdraw should be allowed
    def withdraw(self, amount: float):
        if self.balance - amount < 0:
            raise RuntimeError("Insufficient funds")
        self.balance -= amount
        print(f"Amount withdrawn. Remaining balance is {self.balance}")


class FixedDepositAccount(BankAccount):
    def __init__(self, b: float):
        super().__init__(b)

    # LSP break! History constraint broken!
    # Parent class behaviour changed: Now withdraw is not allowed.
    # This class will break client code that relies on withdraw.
    def withdraw(self, amount: float):
        raise RuntimeError("Withdraw not allowed in Fixed Deposit")


if __name__ == "__main__":
    bankAccount = BankAccount(100)
    bankAccount.withdraw(100)
