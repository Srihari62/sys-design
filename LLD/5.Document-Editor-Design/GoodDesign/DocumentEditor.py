from abc import ABC, abstractmethod

# -----------------------------
# Abstraction for document elements
# -----------------------------
class DocumentElement(ABC):
    @abstractmethod
    def render(self):
        pass


# -----------------------------
# Concrete TextElement
# -----------------------------
class TextElement(DocumentElement):
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text


# -----------------------------
# Concrete ImageElement
# -----------------------------
class ImageElement(DocumentElement):
    def __init__(self, image_path):
        self.image_path = image_path

    def render(self):
        return f"[Image: {self.image_path}]"


# -----------------------------
# NewLineElement
# -----------------------------
class NewLineElement(DocumentElement):
    def render(self):
        return "\n"


# -----------------------------
# TabSpaceElement
# -----------------------------
class TabSpaceElement(DocumentElement):
    def render(self):
        return "\t"


# -----------------------------
# Document class - holds elements
# -----------------------------
class Document:
    def __init__(self):
        self.document_elements = []

    def add_element(self, element: DocumentElement):
        self.document_elements.append(element)

    def render(self):
        return "".join(element.render() for element in self.document_elements)


# -----------------------------
# Persistence Abstraction
# -----------------------------
class Persistence(ABC):
    @abstractmethod
    def save(self, data):
        pass


# -----------------------------
# FileStorage implementation
# -----------------------------
class FileStorage(Persistence):
    def save(self, data):
        try:
            with open("document.txt", "w") as file:
                file.write(data)
            print("Document saved to document.txt")
        except:
            print("Error: Unable to open file for writing.")


# -----------------------------
# Placeholder DBStorage
# -----------------------------
class DBStorage(Persistence):
    def save(self, data):
        # Future DB saving logic
        pass


# -----------------------------
# DocumentEditor (client interface)
# -----------------------------
class DocumentEditor:
    def __init__(self, document: Document, storage: Persistence):
        self.document = document
        self.storage = storage
        self.rendered_document = ""

    def add_text(self, text):
        self.document.add_element(TextElement(text))

    def add_image(self, image_path):
        self.document.add_element(ImageElement(image_path))

    def add_newline(self):
        self.document.add_element(NewLineElement())

    def add_tab_space(self):
        self.document.add_element(TabSpaceElement())

    def render_document(self):
        if not self.rendered_document:
            self.rendered_document = self.document.render()
        return self.rendered_document

    def save_document(self):
        self.storage.save(self.render_document())


# -----------------------------
# Client usage example
# -----------------------------
if __name__ == "__main__":
    document = Document()
    storage = FileStorage()

    editor = DocumentEditor(document, storage)

    # Add content
    editor.add_text("Hello, world!")
    editor.add_newline()
    editor.add_text("This is a real-world document editor example.")
    editor.add_newline()
    editor.add_tab_space()
    editor.add_text("Indented text after a tab space.")
    editor.add_newline()
    editor.add_image("picture.jpg")

    # Render and print
    print(editor.render_document())

    # Save to file
    editor.save_document()
