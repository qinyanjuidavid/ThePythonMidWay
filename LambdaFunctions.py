def identity(x):
    return x
i=identity("John Doe")
print(i)

print((lambda x:x+1)(2))
print((lambda name:name) ("John"))
#Lambda is an expression thus it can be named
add_one=lambda x :x +1
print(add_one(2))
print(add_one(5))
#eg
identity=lambda name:"My name is {}.".format(name)
print(identity("John Doe"))
print(identity("Jane Doe"))
#eg2
identity=lambda name,age,department:"My name is {}, I am {} years old. I am in the {} department".format(name,age,department)
i1=identity("Angie Valdosa",28,"Human Resource")
print(i1)
full_name=lambda first,last:"Full name: {} {}".format(first.title(),last.title())
print(full_name("Guido","Van rossum"))
displayAge=lambda age=18:age #Using arguments or the default values
print(displayAge(20))
print(displayAge())
#Anonymous Functions
_=lambda x,y:x+y #Anonymous function are not bonded to a variable
print(_(1,2))#Invoking the function
#Lambda as a High order Function
high_ord_func=lambda x,func:x+func(x)
print(high_ord_func(5,lambda x:x*x))
print(high_ord_func(6,lambda x:x*x))
#Python Lambda and Regular Functions
import dis
add=lambda x,y:x+y
print(type(add))
print(dis.dis(add))
print(add)

def add(x,y):
    return x+y
print(type(add))
print(dis.dis(add))
print(add)

div_zero=lambda x:x/1
print(div_zero(2))
#Arguments
print((lambda x,y,z:x+y+z) (1,2,3))
print((lambda x,y,z=3:x+y+z)(1,2))
print((lambda x,y,z=3:x+y+z)(1,y=2))
print((lambda *args:sum(args))(1,2,3,4,5))
print((lambda **kwargs:sum(kwargs.values()))(one=1,two=2,three=3))
print((lambda x,*,y=0,z=0:x+y+z)(1,y=2,z=3))
#Decorators
def some_decorator(f):
    def wrapper(*args,**kwargs):
        print(f"Calling function '{f.__name__}'")
        return f(args)
    return wrapper
@some_decorator
def decorated_function(x):
    print(f"With argument '{x}'")
decorated_function("Jane Doe")

#Defining the second decorator
def trace(f):
    def wrap(*args,**kwargs):
        print(f"[TRACE] func: {f.__name__},args: {args}, kwargs: {kwargs}")
        return f(*args,**kwargs)
    return wrap

@trace
def add_two(x):
    return x+2
print(add_two(5))

#Defining decorators in lambda function
def Trace2(f):
    def wrapper(*args,**kwargs):
        print("***This is my decorator.***")
        return f(*args,**kwargs)
    return wrapper
print((Trace2(lambda name,age,department:"My name is {}, I am {} years old. I work in the {} department.".format(name,age,department)))("Angela Valdes",28,"Human Resource"))
identity=Trace2(lambda name,age,department:"My name is {}, I am {} years old. I work in the {} department.".format(name,age,department))
print(identity("John Doe",28,"Human Resource"))
#Single expression
print((lambda x:
      (x%2 and 'odd' or 'even'))(3))
print((lambda x:x*3)(3))