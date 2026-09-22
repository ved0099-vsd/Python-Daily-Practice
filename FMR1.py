from MarvellousLibrary import filterX,mapX,reduceX

Odd = lambda No : No % 2 != 0
Double = lambda No : No * 2
Sum = lambda No1,No2 : No1 + No2

def main():
    Data = [12,35,65,44,98,55,99]
    print("Data is :",Data)

    FData = list(filterX(Odd,Data))
    print("Data after Filtering is :",FData)

    MData = list(mapX(Double,FData))
    print("Data after Mapping is :",MData)

    RData = reduceX(Sum,MData)
    print("Data after reducing is :",RData)

if __name__ == "__main__":
    main()