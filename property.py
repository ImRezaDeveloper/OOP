class Employee():
    salary = 3000
    total_emp = 0
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Employee.total_emp += 1

    
    # property => this decorator do make full_name method to attribute
    @property
    def full_name(self):
        return f"My fullname is {self.first_name} - {self.last_name}"
    
    @full_name.setter
    def change_full_name(self, new_full_name):
        self.first_name, self.last_name = new_full_name.split(" ")
    
    @full_name.deleter
    def delete_full_name(self):
        self.first_name = None
        self.last_name = None
        
emp1 = Employee("reza", "papi")
emp2 = Employee("fardad", "farahzad")
print(emp1.full_name)
emp2.change_full_name = "reza zamani"
print(emp2.full_name)

del emp1.delete_full_name
print(emp1.full_name)