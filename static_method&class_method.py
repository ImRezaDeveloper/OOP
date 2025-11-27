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

emp1 = Employee("reza", "papi")

print("befor")
print(emp1.full_name(), " - ", emp1.salary)

Employee.raise_salary(5000)

print("after")
print(emp1.full_name(), " - ", emp1.salary)
