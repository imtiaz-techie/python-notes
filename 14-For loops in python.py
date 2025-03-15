#learning 1:
name="Minar"
for i in name:
    print(i)
    if(i=="n"):
        print("this is a special code")


#learning 2:
colours=["red","green","blue"]
for i in colours:
    print(i)
 

#learning 3:
colours=["red","green","blue"]
for color in colours:
    print(color)
    for i in color:
        print(i)
    print()    #eta ek ekta iteration er por newline print korbe
   
  
#learning 4:
1.
for k in range(5):              #indexing hobe- 0 to n-1/4      
   print(k)
2.
for k in range(1,5):             #indexing hobe- 1 to n-1/4      
   print(k)
3.
for k in range(1,12,3):         #it prints 1,4,7,10
   print(k)


#learning 5: string ke list baniye erpor list item gula print korlam
a="My name is Minar"
b=a.split()
for i in b:
    print(i)
