from abc import ABC, abstractmethod

# Interface for Document Reader
class IDocumentReader(ABC):
    @abstractmethod
    def unlock_pdf(self, file_path: str, password: str):
        pass

# Concrete Class: Reads the PDF (simulated)
class RealDocumentReader(IDocumentReader):
    def unlock_pdf(self, file_path: str, password: str):
        print(f"[RealDocumentReader] Unlocking PDF at: {file_path}")
        print(f"[RealDocumentReader] PDF unlocked successfully with password: {password}")
        print("[RealDocumentReader] Displaying PDF content...")

# User class with membership status
class User:
    def __init__(self, name: str, is_premium: bool):
        self.name = name
        self.premium_membership = is_premium

# Proxy Class: Controls access to RealDocumentReader
class DocumentProxy(IDocumentReader):
    def __init__(self, user: User):
        self._real_reader = RealDocumentReader()
        self._user = user

    def unlock_pdf(self, file_path: str, password: str):
        if not self._user.premium_membership:
            print("[DocumentProxy] Access denied. Only premium members can unlock PDFs.")
            return

        # Forwarding the request to the real reader
        self._real_reader.unlock_pdf(file_path, password)

# Client code
def main():
    user1 = User("Rohan", False)  # Non Premium User
    user2 = User("Rashmi", True)   # Premium user

    print("== Rohan (Non-Premium) tries to unlock PDF ==")
    doc_reader1 = DocumentProxy(user1)
    doc_reader1.unlock_pdf("protected_document.pdf", "secret123")

    print("\n== Rashmi (Premium) unlocks PDF ==")
    doc_reader2 = DocumentProxy(user2)
    doc_reader2.unlock_pdf("protected_document.pdf", "secret123")

if __name__ == "__main__":
    main()
