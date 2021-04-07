#Functions
def add_one(number):
    return number+1
print(add_one(5))
print(add_one(88))
#First-class objects
def say_hello(name):
    return f"Hello {name}"
print(say_hello("John Doe"))

def be_awesome(name):
    return f"Yo {name},together we are the awesomest!"
print(be_awesome("Jane Doe"))

def greet_bob(greeter_func):
    return greeter_func("Bob")
print(greet_bob(say_hello))
print(greet_bob(be_awesome))
#Inner Functions
#This are functions inside other functions
def parent():
    print("Printing from the parent() function")
    def first_child():
        print("Printing from the first_child() function")
    def second_child():
        print("Printing from the second_child() function")
    first_child()
    second_child()
parent()
#Returning Functions from Function
def parent(num):
    def first_child():
        return "Hi, I am John Doe"
    def second_child():
        return "Call me Jane Doe"
    if num==1:
        return first_child()
    else:
        return second_child()
print(parent(1))
print(parent(2))
#Simple decorators
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Something is happening before the function is called.")
        func(*args,**kwargs)
        print("Something is happening after the function is called.")
    return wrapper
def say_whee():
    print("Whee")
say_whee=my_decorator(say_whee)
say_whee()

#Second decorator
from datetime import datetime
def not_during_the_night(func):
    def wrapper(*args,**kwargs):
        if datetime.now().hour<23:
            func(*args,**kwargs)
        else:
            print("Hello")
            # pass#The Neighbours are asleep
    return wrapper
def say_whee():
    print("Whee!")
say_whee=not_during_the_night(say_whee)
say_whee()
print()
#Syntactic sugar
#We ll make use of the pie syntax
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Something is happening before the function is called.")
        func(*args,**kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")
say_whee()
print()
#Reusing decorators
def do_twice(func):
    def wrapper_do_twice(*args,**kwargs):
        func()
        func()
    return wrapper_do_twice

@do_twice
def say_whee():
    print("Whee!")
say_whee()
#Decorating Functions with Arguments
print()
def do_twice(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper

@do_twice
def greet(name):
    print("Hello {}".format(name))
greet("Angie Valdosa")
#Using the return instead of the print
def do_twice(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper

@do_twice
def say_whee(name):
    return "Hello, {}".format(name)
print(say_whee("Jamie Saint Patrick"))
#Introspection
from functools import wraps
def do_twice(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        func(*args,**kwargs)
    return wrapper
@do_twice
def say_whee(name):
    print("Hello, {}".format(name)) #Introspection -->The ability of a function to know its details
say_whee("John Doe")
print(say_whee.__name__)
#Real world examples
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        value=func(*args,**kwargs)
        return value
    return wrapper
#Timing Functions
from functools import wraps
import time
def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time=time.perf_counter()
        rv=func(*args,**kwargs)
        end_time=time.perf_counter()
        run_time=end_time-start_time
        print("Function: {!r} finished in {} secs".format(func.__name__,run_time))
        return rv
    return wrapper
@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(100)])
waste_some_time(1)
waste_some_time(999)
#Decorating Classes
#Some of the most commonly used  class decorators are @property,@classmethod amd the @staticmethod
#The @classmethod and @staticmethod are used to decorate the methods in a class
#The @property decorators is uded to customize getters and setters
from functools import wraps
import time
print()
def timer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time=time.time()
        rv=func(*args,**kwargs)
        end_time=time.time()
        run_time=end_time-start_time
        print("Function: {} finished in {} secs".format(func.__name__,run_time))
        return rv
    return wrapper
@timer
class TimeWaster(object):
    def __init__(self,max_num):
        self.max_num=max_num
    def waste_time(self,num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(self.max_num)])
tw=TimeWaster(5)
tw.waste_time(56)
#Nesting Decorators
#Lets add and substract numbers using decorators
from functools import wraps
def CallOnce(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        rv=func(*args,**kwargs)
        return rv
    return wrapper
def CallTwice(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper
@CallOnce
@CallTwice
def RealFunc(num1,num2):
    sub=num1-num2
    return sub
print(RealFunc(56,5))
