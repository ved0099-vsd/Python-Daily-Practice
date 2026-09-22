from functools import reduce

Odd = lambda No : No % 2 != 0

Square = lambda No : No * No

Sum = lambda No1, No2 : No1 + No2

def main():
    Data = [1,2,3,4,5,6,7,8,12,32,34,45,65,67,78,98,65,66,45,5,54]
    print("Data is : ",Data)

    FData = list(filter(Odd,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Square,FData))
    print("Data after Mapping is : ",MData)

    RData = reduce(Sum,MData)
    print("Data after Reduce is : ",RData)


if __name__ == "__main__":
    main()