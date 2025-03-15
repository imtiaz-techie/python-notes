# Tuples are unchangable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")      #add item ("Spain", "Italy", "India", "England", "Germany","Russia")
temp.pop(3)                #remove item ("Spain", "Italy", "India", "Germany","Russia")
temp[2] = "Finland"       #change item   ("Spain", "Italy", "Finland", "Germany","Russia")
countries = tuple(temp)
print(countries)



# However, we can directly concatenate two tuples without converting them to list.
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)


tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3,3,3)
res = tuple1.count(3)
print(res)
res = tuple1.index(3)
print(res)
res = tuple1.index(3, 4, 8)  # (4-8) er moddhe 3 er index
print(res)
res = len(tuple1)
print(res)