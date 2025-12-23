from abc import ABC, abstractmethod


# Observer Interface
class ISubscriber(ABC):
    @abstractmethod
    def update(self):
        pass


# Observable Interface (Channel interface)
class IChannel(ABC):
    @abstractmethod
    def subscribe(self, subscriber):
        pass

    @abstractmethod
    def unsubscribe(self, subscriber):
        pass

    @abstractmethod
    def notify_subscribers(self):
        pass


# Concrete Subject: YouTube Channel
class Channel(IChannel):
    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.latest_video = ""

    # Add subscriber (avoid duplicates)
    def subscribe(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    # Remove subscriber
    def unsubscribe(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    # Notify all subscribers
    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update()

    # Upload a new video
    def upload_video(self, title):
        self.latest_video = title
        print(f'\n[{self.name} uploaded "{title}"]')
        self.notify_subscribers()

    # Get video data
    def get_video_data(self):
        return f"\nCheckout our new Video : {self.latest_video}\n"


# Concrete Observer: Subscriber
class Subscriber(ISubscriber):
    def __init__(self, name, channel):
        self.name = name
        self.channel = channel

    # Called by Channel
    def update(self):
        print(f"Hey {self.name},{self.channel.get_video_data()}", end="")


# Client Code
if __name__ == "__main__":
    # Create channel
    channel = Channel("CoderArmy")

    # Create subscribers
    subs1 = Subscriber("Varun", channel)
    subs2 = Subscriber("Tarun", channel)

    # Subscribe users
    channel.subscribe(subs1)
    channel.subscribe(subs2)

    # Upload first video
    channel.upload_video("Observer Pattern Tutorial")

    # Unsubscribe Varun
    channel.unsubscribe(subs1)

    # Upload second video
    channel.upload_video("Decorator Pattern Tutorial")
