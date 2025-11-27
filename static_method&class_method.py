import datetime
class Employee():
    salary = 3000
    total_emp = 0
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Employee.total_emp += 1
    
    def full_name(self):
        return f"My fullname is {self.first_name} - {self.last_name}"
    
    @classmethod
    def raise_salary(cls, new_salary):
        if type(new_salary) == int:
            cls.salary = new_salary
    
    @classmethod
    def create_from_string(cls, your_string):
        first_name, last_name = your_string.split('-')
        return cls(first_name, last_name)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee("reza", "papi")
emp2 = Employee.create_from_string("fardad-papi")

date = datetime.date(2025, 11, 29)
print(emp2.is_workday(date))

print("befor")
print(emp1.full_name(), " - ", emp1.salary)
print(emp2.full_name())

Employee.raise_salary(5000)

print("after")
print(emp1.full_name(), " - ", emp1.salary)
