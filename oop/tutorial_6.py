## Property Decorators - Getters, Setters, and Deleters

class Employee:

    #Define method
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@comp.vn'
    @property 
    # Example of a getter
    #make accessing a method syntax like accessing an attribute syntax (without ()) 
    def email(self): 
        return '{}.{}@comp.vn'.format(self.first, self.last)    
    
    @property
    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')
emp_2 = Employee('C', 'A')

emp_1.fullname = 'Tung Nguyen'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname)
print(emp_2.fullname)