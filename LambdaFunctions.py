def identity(x):
    return x
i=identity("John Doe")
print(i)

print((lambda x:x+1)(2))
print((lambda name:name) ("John"))
#Lambda is an expression thus it can be named
