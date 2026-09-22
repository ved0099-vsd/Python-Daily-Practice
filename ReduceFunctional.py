# Functional = Lambda

from functools import reduce

CheckEven = lambda No : No % 2 == 0

Increment = lambda No : No + 1

Addition = lambda No1,No2 : No1 + No2

def main():
    Data = [24,2,23,65,76,78,65,54,90]
    print("Data is : ",Data)

    FData = list(filter(CheckEven,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Increment,FData))
    print("Data after mapping is : ",MData)

    RData = reduce(Addition,MData)
    print("Data after Reduce is : ",RData)

if __name__ == "__main__":
    main()