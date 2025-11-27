class Employee:
    salary = 3000
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hello(self, name):
        return f'hello {name}'
        
emp1 = Employee("Fardad", 29)
emp2 = Employee("Reza", 20)

print(emp1.name, emp1.age, emp1.salary, emp1.hello('Reza'))
emp2.salary = 3500
print(emp2.name, emp2.age, emp2.salary)
