from functools import reduce

Even = lambda No : No % 2 == 0

Double = lambda No : No * 2

Sum = lambda No1,No2 : No1 + No2

def main():
    Data = [42,21,56,76,90,58,55,34,44,89]
    print("Data is : ",Data)

    FData = list(filter(Even,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Double,FData))
    print("Data after Map is : ",MData)

    RData = reduce(Sum,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()