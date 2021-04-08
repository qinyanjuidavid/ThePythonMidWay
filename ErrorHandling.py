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


try:
    with open("displays.log") as file:
        read_data=file.read()
        print(read_data)
except:
    print("Coult not open displays.log")
#The displays.log does not exist thus an exception is raised
try:
    with open('displays.log') as file:
        read_data=file.read()
        print(read_data)
except FileNotFoundError as fnf_error:
    print(fnf_error)
print()
# Try, Except and else clause
def linux_interaction():
    assert ("linux" in sys.platform)
    print("Doing Something")
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('displays.log') as file:
            read_data=file.read()
            print(read_data)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
#Try, Except, Finally
#Finally helps us in cleaning the codes
import sys
def linux_interaction():
    assert ('linux' in sys.platform)
    print("Doing Something")
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open("displays.log") as file:
            read_data=file.read()
            print(read_data)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print("Cleaning up, irrespective of any exception..")
#Resource II
#Errors cant be handled eg Syntax error
#Exceptions can be handled during run time
def recursion():
    return recursion()
try:
    recursion()
except RecursionError as error:
    print(error)

