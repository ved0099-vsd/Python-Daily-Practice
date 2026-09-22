# 1. Filter → Which elements should I keep?
# 2. Map    → What should I do to each kept element?
# Reduce → How should I combine them?


#Every program follows the same structure:

# FData = list(filter(Check, Data))

# MData = list(map(Operation, FData))

# RData = reduce(Operation, MData)


from functools import reduce

Positive = lambda No : No > 0

Square = lambda No : No * No

Sum = lambda No1,No2 : No1 + No2

def main():
    Data = [21,-3,-6,-53,68,-87,0,33]
    print("Data is : ",Data)

    FData = list(filter(Positive,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Square,FData))
    print("Data after Mapping is : ",MData)

    RData = reduce(Sum,MData)
    print("Data after Reducing is : ",RData)

if __name__ == "__main__":
    main()