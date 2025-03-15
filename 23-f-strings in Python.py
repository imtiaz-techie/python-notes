# String formatting:
letter="my name is {} and i am from {}"
name="minar"
country="Bangladesh"
print(letter.format(name,country))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49.000875))

#to make it more beautiful here is f-string:
val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'minar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")

price=45.63885757383
print(f"for only {price:.2f} you can get the book!")


#to print the syntex of fstring,it will be much needed in carrer
print(f"my name is {{dj}} and i am from {{bj2}}")