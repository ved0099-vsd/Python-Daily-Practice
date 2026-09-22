from functools import reduce

less10 = lambda No : No > 10

Add = lambda No : No + 5

Sum = lambda No1,No2 : No1 + No2

def main():
    Data = [32,54,3,3,5,67,77,9,67,5,4]
    print("Data is : ",Data)

    FData = list(filter(less10,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Add,FData))
    print("DaTA after Mapping is : ", MData)

    RData = reduce(Sum,MData)
    print("Data after Reduce is : ",RData)


if __name__ == "__main__":
    main()