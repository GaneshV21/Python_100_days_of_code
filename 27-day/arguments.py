#default arguments:
# def addd(a,b=2,c=3):
#     print(a+b+c)

# addd(1) # -- 6
# addd(1,4) # -- 8
# addd(2,3,4) #-- 9

# unlimited arguments:
# def add(*args):
#     print(sum(args))
# add(3,4,5,6,7,8,9) # -- 42 -- type -- tuple


#keywords arguments -- unlimited keywords arguments
def calculate(n,**kwargs):
    print(kwargs) # -- {'add': 3, 'multiply': 5}
    n+=kwargs['add']
    n*=kwargs['multiply']
    print(n) # -- 25
calculate(2,add=3,multiply=5)

class car():
    def __init__(self,**kwargs):
        self.make=kwargs['make']
        self.model=kwargs['model']

my_car=car(make="nissan",model="PC6")
print(my_car.make)


# if i am not passing model or make means it gives error
# my_car1=car(make="nissan")
# self.model=kwargs['model']
#                ~~~~~~^^^^^^^^^
# KeyError: 'model'

#instead of this use get method to get the data from kwargs.it gives not error it gives none:

class cars():
    def __init__(self,**kwargs):
        self.make=kwargs.get('make')
        self.model=kwargs.get('model')

my_car2=cars(make="nissan")
print(my_car2.model) # -- None




