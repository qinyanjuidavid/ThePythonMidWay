#Writing in files
f=open("test.txt",'w')
f.write("Hello Friend,,,")
f.write("My name is John Doe")
f.close()
w=open("test.txt","w")
w.write("Hello World, \n")
w.write("My name is John Doe...")
w.close()

# number_of_students=eval(input("Enter the number of students:"))
number_of_students=0
for i in range(number_of_students):
    m=open("ClassRed.txt",'w')
    students_name=input("Enter the name of the student:")
    english=eval(input("English:"))
    kiswahili=eval(input("Kiswahili:"))
    maths=eval(input("Mathematics:"))
    science=eval(input("Science:"))
    sst=eval(input("Social Studies&CRE:"))
    total=english+kiswahili+maths+science+sst
    average=total/5
    m.write("""
    {}. Students Name: {}
    English: {}
    Kiswahili: {}
    Mathematics: {}
    Science: {}
    Social Studies: {}
    Total: {}
    Avg Marks: {}""".format(i+1,students_name,english,kiswahili,maths,science,sst,total,average))
    m.close()
#Reading Binary Files
f=open("coderpass.png","r+b")
print(f)
f.close()
try:
    f=open('encoded.txt','w',encoding="utf-8")
    f.write("Hello Friend,")
finally:
    f.close()
with open("test.txt",'w',encoding='utf-8') as f:
    f.write("Hello friend....")
with open('test.txt','w',encoding='utf-8') as f:
    f.write("This is my first line\n")
    f.write("This line\n")
    f.write("Contains only three lines.")
#Reading files in Python
f= open("test.txt","r",encoding="utf-8")
# print(f.read())
print(f.read(7))
print(f.read())
print(f.tell())
print(f.seek(1))
print(f.read())
f.close()
with open("test.txt",'r',encoding="utf-8") as f:
    for line in f:
        print(line,end=",")

#Using the readline() function
print()
with open('text.txt','w',encoding="utf-8") as f:
    f.write("My name is John Doe,\n")
    f.write("I am 28 years old.\n")
    f.write("I work in the human resource department.")
with open("text.txt",'r',encoding="utf-8") as f:
    # print(f.read())
    print(f.readlines())
