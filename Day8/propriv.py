class Employee:
    def __init__(self, salary, bonus):
        self._salary = salary      
        self.__bonus = bonus       

    def get_bonus(self):
        return self.__bonus


class Manager(Employee):
    def show_details(self):
        print("Salary:", self._salary)
        print("Bonus:", self.get_bonus()) #using getter method to access private attribute
        print("Bonus using name mangaling inside class: ", self._Employee__bonus) # Accessing private attribute from inside the class using name mangling [Note: self.Employee__bonus]

m = Manager(50000, 10000)
m.show_details()
print("Bonus using name mangaling outside class: ",m._Employee__bonus) # Accessing private attribute from outside the class using name mangling [Note: m._Employee__bonus where m is the instance of the class]

#Format of name mangling: _ClassName__attributeName/ _ClassName__variableName (private attribute/variable)