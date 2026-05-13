from abc import ABC, abstractmethod
from typing import Optional

class IImage(ABC):
    @abstractmethod
    def display(self):
        pass

class RealImage(IImage):
    def __init__(self, filename: str):
        self._filename = filename
        # Heavy Operation
        print(f"[RealImage] Loading image from disk: {self._filename}")

    def display(self):
        print(f"[RealImage] Displaying {self._filename}")

class ImageProxy(IImage):
    def __init__(self, filename: str):
        self._filename = filename
        self._real_image: Optional[RealImage] = None

    def display(self):
        # Lazy initialization of RealImage
        if self._real_image is None:
            self._real_image = RealImage(self._filename)
        self._real_image.display()

def main():
    image1 = ImageProxy("sample.jpg")
    image1.display()

if __name__ == "__main__":
    main()
