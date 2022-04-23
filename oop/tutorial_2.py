## class variable are class that are shared among all instances of a class
## instance variable

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

        Employee.num_of_emps += 1 #we use class(Employee) here but not instance(self) because we want the number of employees be the same for every instance, regardless of instance
    
    def fullname(self): ## this is a method
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        #self.pay = int(self.pay * Employee.raise_amount) #this will take the class variable and we can only change the raise_amount if we change it in its class.
        #or
        self.pay = int(self.pay * self.raise_amount) #this will take the instance variable and we can change the raise_amount of the instance regardless of the raise_amount in the variable in class.

print(Employee.num_of_emps)

emp1 = Employee('Tung', 'Nguyen', 50000)
emp2 = Employee('Test', 'User', 60000)

emp1.raise_amount = 1.06 #this will change the value of raise_amount in instance emp1, but only in emp1

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

print(emp1.num_of_emps)
print(emp1.num_of_emps)
print(Employee.num_of_emps)

