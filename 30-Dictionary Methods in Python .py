#learning 1:update()
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}
ep1.update(ep2)
print(ep1)


#learning 2:clear()
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)

#learning 3:pop()
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)

#learning 4:popitem() The popitem() method removes the last key-value pair from the dictionary.
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)

#learning 5:del
#way 1:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)

#way 2:
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)
