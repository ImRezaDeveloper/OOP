# Person
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"
    
class Employee(Person):
    
    def __init__(self, first_name, last_name, position):
        super().__init__(first_name, last_name)
        self.position = position
    
    def get_job(self):
        return f"My fullname is {self.first_name} - {self.last_name} , i'm {self.position}"
    
emp1 = Employee('reza', 'papi', 'backend developer')
print(emp1.get_job())

# Manager
class Manager:
    """
        can be hire anyone at company
    """
    def authority(self):
        return f'ca be hire or fire anyone'

class CTO(Employee, Manager):
    
    salary = 6000
    
    def get_job(self):
        return f"My fullname is {self.first_name} - {self.last_name} , i'm {self.position}"
    
emp2 = CTO('Fardad', 'Farahzad', 'CTO')

print(emp2.salary)
print(emp2.get_job())
print(emp2.authority())