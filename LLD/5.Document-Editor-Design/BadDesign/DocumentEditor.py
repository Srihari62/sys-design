class DocumentEditor:
    def __init__(self):
        self.document_elements = []
        self.rendered_document = ""

    # Adds text as a plain string
    def add_text(self, text):
        self.document_elements.append(text)

    # Adds an image represented by its file path
    def add_image(self, image_path):
        self.document_elements.append(image_path)

    # Renders the document by checking extensions at runtime
    def render_document(self):
        if not self.rendered_document:
            result = ""
            for element in self.document_elements:
                if element.endswith(".jpg") or element.endswith(".png"):
                    result += f"[Image: {element}]\n"
                else:
                    result += element + "\n"
            self.rendered_document = result

        return self.rendered_document

    # Saves document to a file
    def save_to_file(self):
        try:
            with open("document.txt", "w") as file:
                file.write(self.render_document())
            print("Document saved to document.txt")
        except:
            print("Error: Unable to open file for writing.")


# Main section
if __name__ == "__main__":
    editor = DocumentEditor()
    editor.add_text("Hello, world!")
    editor.add_image("picture.jpg")
    editor.add_text("This is a document editor.")

    print(editor.render_document())

    editor.save_to_file()
