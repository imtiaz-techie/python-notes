# learning 1:
# Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.
s = {2, 4, 2, 6}
print(s)


# learning 2:
# the items of set occur in random order and hence they cannot be accessed using index numbers.
info = {"Carla", 19, False, 5.9, 19}
print(info)   #output:{False, 19, 5.9, 'Carla'}

# learning 3:
info={}
print(type(info))    #output: dictionary
info=set()
print(type(info))    #output:set


# learning 4: access into a set
info = {"Carla", 19, False, 5.9, 19}
for value in info:
  print(value)