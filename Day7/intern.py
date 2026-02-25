from abc import ABC, abstractmethod
class Employee(ABC):
    
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary
    
    def calculate_salary(self):
        return self.monthly_salary

class Intern(Employee):
    
    def __init__(self, name, emp_id, stipend, duration_months):
        super().__init__(name, emp_id)
        self.stipend = stipend
        self.duration_months = duration_months
    
    def calculate_salary(self):
        return self.stipend * self.duration_months

emp = FullTimeEmployee("Alice", 101, 50000)
intern = Intern("Bob", 202, 10000, 3)

print(f"{emp.name}'s Salary:", emp.calculate_salary())
print(f"{intern.name}'s Total Stipend:", intern.calculate_salary())