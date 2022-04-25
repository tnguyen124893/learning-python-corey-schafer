# regular (instance) methods <> class methods <> static methods
class Employee:

    #Define class variable
    raise_amount = 1.04
    num_of_emps = 0

    #Define method
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comp.vn'

        Employee.num_of_emps += 1
    
    def fullname(self): ## this is a method
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod ##class method take Class as the first and default argument, regular method take instance as the first and default argument
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('Tung', 'Nguyen', 50000)
emp2 = Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.06) 
#this is equal to
# emp1.set_raise_amt(1.06) #but not many people do this

print(emp1.raise_amount)
print(emp1.raise_amount)
print(Employee.raise_amount)

###########
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2020, 9, 11)

print(Employee.is_workday(my_date))