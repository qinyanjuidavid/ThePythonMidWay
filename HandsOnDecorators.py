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






