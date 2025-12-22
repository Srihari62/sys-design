from strategies.payment_strategy import PaymentStrategy


class CreditCardPaymentStrategy(PaymentStrategy):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def pay(self, amount: float):
        masked = "**** **** **** " + self.card_number[-4:]
        print(f"Paid ₹{amount} using Credit Card ({masked})")
