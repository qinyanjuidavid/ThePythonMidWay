#PRNG-->Pseudorandom Number Generator(The random numbers generated using Python,,Done by software)
#TRNG-->True Random Number Generator eg. Tossing a die in the air(Done by hardware)
class NotSoRandom(object):
    def seed(self,a=3):
        self.seedval=a
    def random(self):
        self.seedval=(self.seedval*3%19)
        return self.seedval
_inst=NotSoRandom()
seed=_inst.seed
random=_inst.random
seed(1234)
print([random() for _ in range(10)])
#Trial in my own way
import random
print(random.random())
l=[]
for i in range(10):
    l.append(i)
print(l)
#Deterministic Random
# random.seed(444)
print(random.random())
print(random.random())
#Randint
r=random.randint(0,10)
print(r)
r1=random.randint(500,5000)
print(r1)
#Random RandRange
print(random.randrange(1,10))
print(random.randrange(100,500))
#Random.uniform
print(random.uniform(20,30))
print(random.uniform(30,40))
#Random.choice, Choice is used with the collective data types
items=["one",'two','three',"four",'five']
print(random.choice(items))
game=["1","X","2"]
print(random.choice(game))
class Add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return self.a + self.other
if __name__=="__main__":
    a=Add(5,6)
    print(a.a+a.b)
#Changed the study material
import random
print(random.randint(0,5))
print(random.random())#It is giving us a float
print(random.random()*100)#We can multiply it, so that we get the output in the range that we want
print(random.random()*1000)#Now it ranges between 0,1000
print(random.randint(0,100))#Same as the above line
#Choice
#Choice is used with the collective data types
l=["Red","Black","Green"]#Using a list
print(random.choice(l))
t=(3.1,5.6,7.9,32.1)#Using a tuple
print(random.choice(t))
# s={"Orange","Banana","Banana","Water Melon","Strawberry"}#Using a set
# print(random.choice(s)) Set can't be used in this case
d={
    "Jamie":32000,
    "Angie":45000,
    "Jane Doe":28000,
    "John Doe":56000
}
# print(random.choice(d)) Dictionaries cant be used with choice
print(d.keys())
d=list(d.keys())
print(random.choice(d))#Thus we have to device a way by converting the keys into a list
from collections import deque
#Lets try using the deque which is almost as similar as a list
name="J"
a=deque(name)
a.append("John Doe")
a.popleft()
a.append("Jane Doe")
a.append("Jamie Saint Patric")
a.append("Angie Valdes")
print(a)
print(random.choice(a))
#Further examples
myList=[2,109,False,10,"Lorem",482,"Ipsum"]
print(random.choice(myList))
#Shuffle
import random
from random import shuffle
x=[[i]for i in range(10)]
random.shuffle(x)
print(x)
l=[]
for i in range(10):
    l.append(i)
shuffle(l)
print(l)
#RandRange
print(random.randint(1,100))#RandRange allows the use of a step unlike the randint
print(random.randrange(0,100,5))#Start,Stop,Step
put=[]
for i in range(2):
   put.append(random.randrange(0,101,5))
print(put)
#Code Example
import random
import itertools
outcomes={
    "head":0,
    "tails":0
}
sides=outcomes.keys()
# print(outcomes.values())
# print(outcomes.keys())
sides=list(sides)
for i in range(1000):
    p=random.choice(sides)
    outcomes[p]+=1
print("Heads:",outcomes['head'])
print("Tail:",outcomes['tails'])
#Learning material two
import random
# random.seed(5)
print(random.random())
print(random.random())
print(random.random())
#Randint
print(random.randint(1,100))
print(random.randint(-10,1))
#RandRange
print(random.randrange(1,10))
print(random.randrange(1,10,2))
print(random.randrange(0,101,10))
#choice
print(random.choice("computer"))
print(random.choice([12,23,45,67,43]))
print(random.choice([12,23,45,67,65,43]))
#Shuffle
n=[12,23,45,67,65,43]
random.shuffle(n)
print(n) #The shuffle method reorders the list
#Example of a code
score=0
while True:
    num=input("Guess a number between 1-50, If it matches with the computer, It's a bingo:")
    try:
        computers_guess=random.randrange(0,50)
        num=int(num)
        if type(num)==int and num>=0 and num<=50:
            print("Not correct, the computer guessed {}.".format(computers_guess))
        if num>=0 and num<=50 and type(num)==int:
            if computers_guess==num:
                print("Congratulations, you are a genius!!")
                score+=1
                print(score)
                c=['Yes','No']
                cont=input("Would you like to continue (Yes/No)?")
                cont.lower()
                if cont==c[0].lower() or cont[0]=="y":
                    continue
                elif cont==c[1].lower() or cont[0]=="n":
                    break
                else:
                    print("Invalid Entry!")
        else:
            print("Please enter a valid integer between 1-50.")
    except:
        print("Please enter an integer")


