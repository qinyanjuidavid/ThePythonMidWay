#The output of one function becomes the input of another function
def add(x):
    return x+2
print(add(5))
def multiply(x):
    return x*2
print(multiply(5))
#Using compostion
def add(x):
    return x+2

add(5)
def multiplication(x):
    return x*2
print(multiplication(add(5)))