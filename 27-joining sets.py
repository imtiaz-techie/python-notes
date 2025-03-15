# 1. union(): prints all items,returns a new set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)             # output:{'Tokyo', 'Madrid', 'Kabul', 'Seoul', 'Berlin', 'Delhi'}


# 2.update(): print all items,adds item into the existing set from another set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)              # output:{'Berlin', 'Madrid', 'Tokyo', 'Delhi', 'Kabul', 'Seoul'}


# 3.intersection():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)             # output: {'Madrid', 'Tokyo'}


# 4.intersection_update():
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)              # output:{'Tokyo', 'Madrid'}


# 5.symmetric_difference and symmetric_difference_update(): (those who are not simillar from both sets)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)             # output:{'Seoul', 'Kabul', 'Berlin', 'Delhi'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)              # output:{'Kabul', 'Delhi', 'Berlin', 'Seoul'}

#6.difference() and difference_update(): prints only items that are only present in the original set and not in both the sets.(jegular mil nai ora original set er moddhe)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)              # output:{'Tokyo', 'Madrid', 'Berlin'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))   # output:{'Tokyo', 'Berlin', 'Madrid'}




