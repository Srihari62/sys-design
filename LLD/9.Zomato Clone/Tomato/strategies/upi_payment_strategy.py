from strategies.payment_strategy import PaymentStrategy


class UpiPaymentStrategy(PaymentStrategy):
    def __init__(self, mobile: str):
        self.mobile = mobile

    def pay(self, amount: float):
        print(f"Paid ₹{amount} using UPI ({self.mobile})")
