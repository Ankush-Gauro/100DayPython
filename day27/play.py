def add(*arg):
    print(type(arg))
    return sum(arg)

sum = add(3,5,6,3,2)
print(sum)

def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)
    n += kwargs['add']
    n *= kwargs['mul']
    return n

sum = calculate(5, add=3, sub=5, mul=6, div=3, mod=2)
print(sum)

class Car():
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')

my_car = Car(make='Nissan', model='GT-R')
print(my_car.make)

