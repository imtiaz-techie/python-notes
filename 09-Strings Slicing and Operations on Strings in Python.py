# learning 1:length of a string using len() function
name = "Minar"
len1 = len(name)
print("The word",name,"has",len(name),"letters")


# learning 2:way 1
a="hola,minar"
print(a[0:6])   #indexing:including 0 but less than 6

# learning 2:way 2
a="hola,minar"
print(a[:6])

print(a[1:4]) # including 1 but not 4

# learning 3:way 1
a="minar"
print(a[0:len(a)-2])   #it means (5-2)=3,(min) print krbe

# learning 3:way 2     
a="minar"
print(a[0:-2])   #same same way 1

# learning 4:
a="minar"
print(a[-3:-1])    #(5-3=2) to (5-1=4) print 2 to 4 (including 2 but less than 4)
