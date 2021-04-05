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