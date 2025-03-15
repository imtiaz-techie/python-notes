def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
    print("I am always executed") # finally na diye print diye show korleo hobe but jokhon funtion nibo tokhon only print dile output e show krbe na finally dite hobe
x = func1()
print(x)

