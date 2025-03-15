#learning 1:
marks=[1,2,3]
list=["Red", "Green", "Blue"]
list1=["Red",4,5, "Blue",True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(list)
print(list1)

# learning 2:
# LIST-INDEXING:
# positive indexing
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])
#negative indexing
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])

# learning 3:
# Check whether an item in present in the list?
marks=[1,3,4,5]
if 4 in marks:            
    print("4 is present")   
else:
    print("4 is not present") 

marks=[1,3,4,5,"minar"]
if "minar" in marks:            
    print("\"minar\" is present")   
else:
    print("\"minar\" is not present")    

# learnig 4:
# check string within a string
if "min" in "minar":
    print("yes")
else:
    print("no")       #serially hote hobe,direct flow milte hobe.tahole yes print korbe

if "mia" in "minar":
    print("yes")
else:
    print("no")

# learning 5:
# we can also print list like that
marks=[1,2,3,5,6,7]
#way 1:print(marks)
#way 2:print(:)
#way 3:print(marks[0:]) 
#way 4:print(marks[1:])      #from 1 to end
#way 5:print(marks[1:4])     #index 1 to 3 print 

# learning 6:
# jump index:present index er sathe addition kore kore oii index er element print korbe
marks=[1,2,3,4,5,6,7,8,9,10,11,12]
print(marks[0:12:2])

# learning 7:list comprehension:
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)





