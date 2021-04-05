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
#Anonymous Functions