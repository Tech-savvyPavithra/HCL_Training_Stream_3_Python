class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading + operator [In python + = __add__ method, - = __sub__ method, * = __mul__ method, / = __truediv__ method]
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)

result = v1 + v2  #v1 is self and v2 is other in __add__ method

print(result)

"""
Operator overloading in Python is done using special methods like __add__, __sub__, __mul__.
Here, we overloaded + to perform vector addition.

Instead of writing Vector, we can write:
return self.__class__(self.x + other.x, self.y + other.y)
"""