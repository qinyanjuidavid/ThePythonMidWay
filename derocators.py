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