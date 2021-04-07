#Raising an exception
x=5
if x>5:
    raise Exception("X should not exceed 5. The value of x was:{}".format(x))
#An exception is raised indicating where the error is
print("Hello friend")

#AssertionError Exception
import sys
def linux_interaction():
    assert ('linux' in sys.platform)
    print("Doing something")
linux_interaction()
#Try and Except block
import sys
def linux_interaction():
    assert ("linux" in sys.platform)
    print("Doing Something")
try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print("The linux function was not excuted")
#The above function only runs on linux
def Divide(n,l):
    a=n/l
    print(a)
Divide(6,3)
try:
    Divide(0,0)
except ZeroDivisionError as error:
    print(error)