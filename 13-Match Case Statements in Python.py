x=int(input("enter a number: "))
match x:
    case 0:
        print("x is zero")
    case 5:
        print("x is five")
    case _:
        print(x)

x=int(input("enter a number: "))
match x:
    case 0:
        print("x is zero")
    case 5:
        print("x is five")
    case _ if x!=6:
        print(x,"is not equel to 90")
    case _ if x!=7:
        print(x,"is not equel to 7")
    case _:
        print(x)    