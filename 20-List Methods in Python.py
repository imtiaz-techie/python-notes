# learning 1:
l = [1,2,3,3,4,5,6]
print(l)
l.append(7)       # just add the numbers
print(l)
l.reverse()       # just reverse the numbers
print(l)
print(l.index(2))  # show the index of the number
print(l.count(3))  # count this number how many times
print(l.copy())    #just copy the list
l.insert(2,5)      #just insert/add the number at index[2]
print(l)
# way - 1:
m = [200,300,400]
l.extend(m)         #it means just add those(m) number at the end of the list of (l)
print(l)
# way - 2:
m = [200,300,400]
k = l+m
print(k)

#learining 2:
num=[1,24,27,40,12,19,38,9,26]
num.sort()       # ascending order
print(num)
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num.sort(reverse=True)     # descending order
print(num)
colors.sort(reverse=True)
print(colors)

