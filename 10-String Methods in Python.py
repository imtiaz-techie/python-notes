#learning 1: uppper
a="Minar"
print(a.upper())

#learning 2: lower
a="Minar"
print(a.lower())

#learning 3: strip-(remove)
a="Minar11!!"
print(a.rstrip("!"))

#learning 4: replace
a="Minar akaja"
print(a.replace("aka","na"))   #aka replaced by na

#learning 5:The split() method splits the given string at the specified instance and returns the separated strings as list items.
a="Minar akaja"
print(a.split())

#learning 6:The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase.
a="tazzriyan ISlaM"
print(a.capitalize())

#learning 7:The center() method aligns the string to the center as per the parameters given by the user.
a="introduction to python!!!!"
print(a.center(400))    
str1 = "Welcome to the Console!!!"            
print(str1.center(50,"."))   #print dot 50/2=25 -> 12+13 in both side

#learning 8:The count() method returns the number of times the given value has occurred within the given string.
a="Minar akaja Minar"
print(a.count("Minar"))
a="AbcAssgA"
print(a.count("A"))

#learning 9:The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
str1 = "Welcome to the Console !!!" #We can even also check for a value in-between the string by providing start and end index positions.
print(str1.endswith("to", 4, 10))

#learning 10:The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
a="we love bangladesh love"
print(a.find("love"))
print(a.find("not"))

#learning 11:The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
a="Harry"
print(a.isalnum())

#learning 12:The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
a="Harry"
print(a.isalpha())

#learning 13:The islower() method returns True if all the characters in the string are lower case, else it returns False.
a="Harry"
print(a.islower())

#learning 14:The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
a="Harry"    #true
print(a.isprintable())
a="Harry\n"   #false
print(a.isprintable())

#learning 15:The isspace() method returns True only and only if the string contains white spaces, else returns False.
a="Harry"
print(a.isspace())

#learning 16:The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
a="Harry Potter Minar"
print(a.istitle())

#learning 17:The isupper() method returns True if all the characters in the string are upper case, else it returns False.
a="WORLD HEALTH ORGANIZATION"
print(a.isupper())

#learning 18:The startswith() method checks if the string starts with a given value. If yes then return True, else return False
a="Python is the most beautiful language"
print(a.startswith("Python "))

#learning 19:The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case
a="pYTHON iS the FUTURE"
print(a.swapcase())

#learning 20:The title() method capitalizes each letter of the word within the string.
a="jerry is the bestfriend of tom"
print(a.title())