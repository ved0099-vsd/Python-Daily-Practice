def CheckOdd(No):
    return No % 2 != 0

def main():
    Data = [32,12,43,54,65,7845,6,64,35453]

    print("Input data is : ", Data)

    FData = list(filter(CheckOdd, Data))

    print("Data after filter is : ", FData)

if __name__ =="__main__":
    main()