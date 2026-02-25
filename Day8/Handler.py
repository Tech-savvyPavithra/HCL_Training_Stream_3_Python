from abc import ABC, abstractmethod

class FileHandler(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass

class TextFileHandler(FileHandler):

    def read(self):
        print("Reading from a text file...")

    def write(self, data):
        print(f"Writing '{data}' to a text file...")

class CSVFileHandler(FileHandler):

    def read(self):
        print("Reading from a CSV file...")

    def write(self, data):
        print(f"Writing '{data}' to a CSV file...")

text = TextFileHandler()
csv = CSVFileHandler()

text.read()
text.write("Hello World")

csv.read()
csv.write("Name,Age")