class Student:
    school_name = "Green Valley School"   # Class Variable

    def __init__(self, name, roll_no):
        self.name = name                  # Instance Variable
        self.roll_no = roll_no            # Instance Variable

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, School: {Student.school_name}") # Class variable accessed using class name

s1 = Student("Alice", 101)
s2 = Student("Bob", 102)

print("Before changing school name:")
s1.display()
s2.display()

Student.school_name = "Sunrise Public School" # Class variable is changed for [all instances] accessed using the class name

print("\nAfter changing school name:")
s1.display()
s2.display()