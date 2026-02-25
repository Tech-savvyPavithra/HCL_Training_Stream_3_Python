class Writer:
    def write(self, text):
        print(f"Writing: {text}")


class Reader:
    def read(self):
        print("Reading content...")


class Editor(Writer, Reader):
    def edit(self, text):
        print("Editing content...")
        self.write(text)
        self.read()

e = Editor()
e.write("Hello World")
e.read()
e.edit("Updated Text")