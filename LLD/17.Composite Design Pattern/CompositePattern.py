from abc import ABC, abstractmethod
from typing import List, Optional

# Base interface for files and folders
class FileSystemItem(ABC):
    @abstractmethod
    def ls(self, indent: int = 0):
        pass

    @abstractmethod
    def open_all(self, indent: int = 0):
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def cd(self, name: str) -> Optional['FileSystemItem']:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def is_folder(self) -> bool:
        pass


# Leaf: File
class File(FileSystemItem):
    def __init__(self, name: str, size: int):
        self._name = name
        self._size = size

    def ls(self, indent: int = 0):
        print(" " * indent + self._name)

    def open_all(self, indent: int = 0):
        print(" " * indent + self._name)

    def get_size(self) -> int:
        return self._size

    def cd(self, name: str) -> Optional[FileSystemItem]:
        return None

    def get_name(self) -> str:
        return self._name

    def is_folder(self) -> bool:
        return False


# Composite: Folder
class Folder(FileSystemItem):
    def __init__(self, name: str):
        self._name = name
        self._children: List[FileSystemItem] = []

    def add(self, item: FileSystemItem):
        self._children.append(item)

    def ls(self, indent: int = 0):
        for child in self._children:
            if child.is_folder():
                print(f"{' ' * indent}+ {child.get_name()}")
            else:
                print(f"{' ' * indent}{child.get_name()}")

    def open_all(self, indent: int = 0):
        print(f"{' ' * indent}+ {self._name}")
        for child in self._children:
            child.open_all(indent + 4)

    def get_size(self) -> int:
        total = 0
        for child in self._children:
            total += child.get_size()
        return total

    def cd(self, target: str) -> Optional[FileSystemItem]:
        for child in self._children:
            if child.is_folder() and child.get_name() == target:
                return child
        # Not found or not a folder
        return None

    def get_name(self) -> str:
        return self._name

    def is_folder(self) -> bool:
        return True


def main():
    # Build file system
    root = Folder("root")
    root.add(File("file1.txt", 1))
    root.add(File("file2.txt", 1))

    docs = Folder("docs")
    docs.add(File("resume.pdf", 1))
    docs.add(File("notes.txt", 1))
    root.add(docs)

    images = Folder("images")
    images.add(File("photo.jpg", 1))
    root.add(images)

    print("--- Listing root ---")
    root.ls()

    print("\n--- Listing docs ---")
    docs.ls()

    print("\n--- Full Tree (openAll) ---")
    root.open_all()

    print("\n--- Changing directory to 'docs' ---")
    cwd = root.cd("docs")
    if cwd is not None:
        cwd.ls()
    else:
        print("Could not cd into docs")

    print(f"\nTotal Size of root: {root.get_size()}")


if __name__ == "__main__":
    main()
