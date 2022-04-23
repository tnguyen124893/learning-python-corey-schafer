# method = function associated with class
# attribute = data associated with class

class Employee:
    def __init__(self, first, last, pay):
        self.first = first ## this is attribute
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@comp.vn'
    
    def fullname(self): ## this is a method
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Tung', 'Nguyen', 50000) # different instance with emp2
emp2 = Employee('Test', 'User', 60000)

print(emp1.email)

#Get full name
print('{} {}'.format(emp1.first, emp1.last))
    #or
print(emp1.fullname()) 
    ## we can access the attribute and method of a instance
    #or
print(Employee.fullname(emp1)) 
    ## we have to pass the instance here
    ## this is what happen in the background