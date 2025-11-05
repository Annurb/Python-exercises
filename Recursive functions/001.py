def recursiva(x):
    if x>0:
        x-=1
        print(x)
        return recursiva(x)
    else:
        print("Final")
    
recursiva(10)