#PYTHON INPUT IS BASICALLY A STRING
# learning 1:
a=input(2)
print(a)

# learning 2:
a=input()
print("My name is",a)

# learning 3:
a=input("Enter your name: ")
print("My name is",a)

# learning 4: in this case,if we give int as a input,it will takes as a string,so it will be concatenated
a=input("Enter first number: ")
b=input("Enter second number: ")
print(a+b)

# learning 5: using typecasting
a=input("Enter first number: ")
b=input("Enter second number: ")
print(int(a)+int(b))
