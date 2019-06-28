class Employee:
    # class variables
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first + self.last}@gmail.com'

    def fullname(self):
        return f'{self.first + self.last}'

    def apply_increment(self):
        self.pay = int(self.pay * raise_amount)

emp1 = Employee("mehedi", "Abdullah", 7000)
emp1.apply_increment()

print(emp1.pay)
