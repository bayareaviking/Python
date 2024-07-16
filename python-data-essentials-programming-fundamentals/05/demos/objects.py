# Quick refresher on Python classes and using objects

class Employee:
    def __init__ (self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob

    def output(self):
        return f"{self.name}\n{self.id}\n{self.dob}"

emp1 = Employee("Marcus Larsson", "12345", "19820511")

print(emp1.output())