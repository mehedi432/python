'''
# Defining a Employee class
class Employee:
    pass

# Instantiate Employee object
emp1 = Employee()
emp2 = Employee()

# Manually add items
emp1.first = "Mehedi"
emp1.last = "Abdullah"
emp1.email = "MehediAbdullah@gmail.com"
emp1.pay = True

# print(type(emp1.pay))

emp2.first = "Masum"
emp2.last = "Abdullah"
emp2.email = "MasumAbdullah@gmail.com"
emp2.pay = True

# print(emp2.pay)
'''

# oop process for this manual process
class Student:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first + last }@company.com'

    def fullname(self, *args):
        return f'{self.first + " " +self.last}'


std = Student("mehedi", "abdullah", 3500)
print(std.email)



