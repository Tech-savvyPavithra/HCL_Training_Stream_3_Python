class MathUtils:

    @staticmethod # Static method needs no instance to be created/called. It belongs to the class and can be called using the class name.
    def add(a, b):
        return a + b

    @classmethod
    def get_class_name(cls):
        return cls.__name__


# Calling WITHOUT creating object
print("Addition:", MathUtils.add(10, 20))
print("Class Name:", MathUtils.get_class_name())

"""
Static Method:
Does NOT use self (self = oject/instance here)
Does NOT use cls
Just a normal function kept inside class for grouping

Class Method:
Receives the class itself as first parameter (cls)
Can access class variables
cls = MathUtils here

Eg:
Class method can be used to change class variables:
class Employee:
    company = "Google"
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name
"""