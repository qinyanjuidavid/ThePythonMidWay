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