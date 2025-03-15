# 1.isdisjoint(): Two sets are said to be disjoint when their intersection is null.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))


# 2.issuperset():The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Tokyo", "Madrid","Berlin"}
print(cities.issuperset(cities3))

# 3.issubset():The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))


# 4.add():If you want to add a single item to the set use the add() method.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)


# 5.update():If you want to add more than one item
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)


# 6.remove()/discard():We can use remove() and discard() methods to remove items form list.
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)





# 7.pop(): removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)


