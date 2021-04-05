#Closure
def outer_function(msg):
    # message=msg
    def inner_function():
        print(msg)
    return inner_function
hi_func=outer_function("Hi")
bye_func=outer_function("Bye")
hi_func()
bye_func()
#Decorator is a function that takes in another function as an argument
def decorator_function(f):
    def wrapper_function(*args,**kwargs):
        print("Function: {}".format(f.__name__))
        return f(*args,**kwargs)
    return wrapper_function

@decorator_function
def Trial():
    print("Hello")
Trial()
#Class Decorators
class DecoratorClass(object):
    def __init__(self,original_function):
        self.original_function=original_function
    def __call__(self,*args,**kwargs):
        print("Function: {}".format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)
@DecoratorClass
def Display():
    print("It worked..")
Display()
print()
#Continuation of the decorator functions
def decorator_function(original_function):
    def wrapper_function(*args,**kwargs):
        print("Function: {}".format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function
@decorator_function
def display():
    print("Display Function ran")
display()

@decorator_function
def display_info(name,age):
    print("display_info ran with arguments {}, {}".format(name,age))
display_info("John Doe",25)
print()
#Practical examples
from functools import wraps
def my_logger(original_function):
    import logging
    logging.basicConfig(filename='{}.log'.format(original_function.__name__),level=logging.INFO)
    @wraps(original_function)
    def wrapper(*args,**kwargs):
        logging.info(
            "Ran with arguments: {}, and kwargs: {}".format(args,kwargs)
        )
        return original_function(*args,**kwargs)
    return wrapper

def my_timer(original_function):
    import time
    @wraps(original_function)
    def wrapper(*args,**kwargs):
        t1=time.time()
        result=original_function(*args,**kwargs)
        t2=time.time()
        t3=t2=t1
        print('{} ran in: {} sec'.format(original_function.__name__,t3))
        return result
    return wrapper
@my_logger
@my_timer
def display(name,age):
    print('display function ran with arguments {} and {}'.format(name,age))
display("John Doe",25)
display("Jane Doe",24)
display("Angie",28)
display("Jamie",30)

