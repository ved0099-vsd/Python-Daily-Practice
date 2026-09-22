from MarvellousLibrary import filterX,mapX,reduceX

Even = lambda No : No % 2 == 0
Increment= lambda No : No + 1
Sum = lambda No1,No2 : No1 + No2

def main():
    Data = [12,34,65,44,2,3,4,5]
    print("Data is : ",Data)

    FData = list(filterX(Even,Data))
    print("Data after Filter is : ", FData)

    MData = list(mapX(Increment,FData))
    print("Data after Mapping is : ",MData)

    RData = reduceX(Sum,MData)
    print("Data after Reduce is : ",RData)

if __name__ == "__main__":
    main()