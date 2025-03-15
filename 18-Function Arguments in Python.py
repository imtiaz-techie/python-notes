# default arguments:
#learning 1:
def num(a=1,b=7):
   print("average is",(a+b)/2)
num(1,11)  #it uses (a=1 & b=11)


#learning 2:
def num(a=1,b=7):  
   print("average is",(a+b)/2)
num(b=11)    #it uses(a=1 & b=11)

#required arguments:
#learning 3:
def person(fname,mname="mohammad",lname="chowdhury"):
   print("hi",fname,mname,lname)
person("Minar")  


#learning4:
def person(fname,mname,lname="chowdhury"):
   print("hi",fname,mname,lname)
person("Shah","minar") 


# VARIABLE LENGTH ARGUMENT:
def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print(sum/len(numbers))  
average(1,2,3)

def name(**name):
   print(type(name))
   print("Hello,", name["fname"], name["mname"], name["lname"])
name(mname="Buchanan", lname="Barnes", fname="James")


# RETURN STATEMENT:      
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)
c=average(1,2,3)
print(c)      