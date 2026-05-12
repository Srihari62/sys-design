from abc import ABC, abstractmethod
from typing import List, Optional

# ============================
#     Notification & Decorators
# ============================

class INotification(ABC):
    @abstractmethod
    def get_content(self) -> str:
        pass

# Concrete Notification: simple text notification.
class SimpleNotification(INotification):
    def __init__(self, msg: str):
        self._text = msg

    def get_content(self) -> str:
        return self._text

# Abstract Decorator: wraps a Notification object.
class INotificationDecorator(INotification):
    def __init__(self, notification: INotification):
        self._notification = notification

# Decorator to add a timestamp to the content.
class TimestampDecorator(INotificationDecorator):
    def get_content(self) -> str:
        # Using a fixed string to match C++ example
        return f"[2025-04-13 14:22:00] {self._notification.get_content()}"

# Decorator to append a signature to the content.
class SignatureDecorator(INotificationDecorator):
    def __init__(self, notification: INotification, signature: str):
        super().__init__(notification)
        self._signature = signature

    def get_content(self) -> str:
        return f"{self._notification.get_content()}\n-- {self._signature}\n\n"

# ============================
#   Observer Pattern Components
# ============================

# Observer interface: each observer gets an update.
class IObserver(ABC):
    @abstractmethod
    def update(self) -> None:
        pass

class IObservable(ABC):
    @abstractmethod
    def add_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass

# Concrete Observable
class NotificationObservable(IObservable):
    def __init__(self):
        self._observers: List[IObserver] = []
        self._current_notification: Optional[INotification] = None

    def add_observer(self, obs: IObserver) -> None:
        self._observers.append(obs)

    def remove_observer(self, obs: IObserver) -> None:
        self._observers.remove(obs)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()

    def set_notification(self, notification: INotification) -> None:
        self._current_notification = notification
        self.notify_observers()

    def get_notification(self) -> Optional[INotification]:
        return self._current_notification

    def get_notification_content(self) -> str:
        if self._current_notification:
            return self._current_notification.get_content()
        return ""

# Concrete Observer 1
class Logger(IObserver):
    def __init__(self, observable: NotificationObservable):
        self._notification_observable = observable

    def update(self) -> None:
        print(f"Logging New Notification : \n{self._notification_observable.get_notification_content()}")

# ============================
#   Strategy Pattern Components (Concrete Observer 2)
# ============================

# Abstract class for different Notification Strategies.
class INotificationStrategy(ABC):
    @abstractmethod
    def send_notification(self, content: str) -> None:
        pass

class EmailStrategy(INotificationStrategy):
    def __init__(self, email_id: str):
        self._email_id = email_id

    def send_notification(self, content: str) -> None:
        print(f"Sending email Notification to: {self._email_id}\n{content}")

class SMSStrategy(INotificationStrategy):
    def __init__(self, mobile_number: str):
        self._mobile_number = mobile_number

    def send_notification(self, content: str) -> None:
        print(f"Sending SMS Notification to: {self._mobile_number}\n{content}")

class PopUpStrategy(INotificationStrategy):
    def send_notification(self, content: str) -> None:
        print(f"Sending Popup Notification: \n{content}")

class NotificationEngine(IObserver):
    def __init__(self, observable: NotificationObservable):
        self._notification_observable = observable
        self._strategies: List[INotificationStrategy] = []

    def add_notification_strategy(self, ns: INotificationStrategy) -> None:
        self._strategies.append(ns)

    def update(self) -> None:
        content = self._notification_observable.get_notification_content()
        for strategy in self._strategies:
            strategy.send_notification(content)

# ============================
#        NotificationService
# ============================

# Singleton class
class NotificationService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NotificationService, cls).__new__(cls)
            cls._instance._observable = NotificationObservable()
            cls._instance._history: List[INotification] = []
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def get_observable(self) -> NotificationObservable:
        return self._observable

    def send_notification(self, notification: INotification) -> None:
        self._history.append(notification)
        self._observable.set_notification(notification)

def main():
    # Create NotificationService.
    notification_service = NotificationService.get_instance()

    # Get Observable
    notification_observable = notification_service.get_observable()
   
    # Create Logger Observer
    logger = Logger(notification_observable)

    # Create NotificationEngine observers.
    notification_engine = NotificationEngine(notification_observable)

    notification_engine.add_notification_strategy(EmailStrategy("random.person@gmail.com"))
    notification_engine.add_notification_strategy(SMSStrategy("+91 9876543210"))
    notification_engine.add_notification_strategy(PopUpStrategy())

    # Attach these observers.
    notification_observable.add_observer(logger)
    notification_observable.add_observer(notification_engine)

    # Create a notification with decorators.
    notification = SimpleNotification("Your order has been shipped!")
    notification = TimestampDecorator(notification)
    notification = SignatureDecorator(notification, "Customer Care")
    
    notification_service.send_notification(notification)

if __name__ == "__main__":
    main()
