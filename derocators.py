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