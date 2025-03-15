for i in range(15):
    if(i==10):
        break                   # full loop break
    print("5 X",i+1,"=",5*(i+1))


for i in range(15): 
    if(i==10):
        print("skip the iteration")
        continue                 # it means only the code above it will be executed(iteration break)
    print("5 X",i+1,"=",5*(i+1))  

# do-while in python
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break