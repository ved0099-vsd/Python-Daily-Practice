def filterX(Task, Elements):    #Task → function such as CheckEven
    Result = []                 #Elements → list of numbers

    for No in Elements:
        Ret = Task(No)          # CheckEven

        if(Ret == True):
            Result.append(No)

    return Result

def mapX(Task, Elements):
    Result = []

    for No in Elements:
        Ret = Task(No)       # Increment(No)
        Result.append(Ret)

    return Result

def reduceX(Task, Elements):
    Sum = 0

    for No in Elements:
        Sum = Task(Sum, No)

    return Sum