def CheckGreater10(No):
    return No > 10

def main():
    Data = [11,4,6,8,23,78]

    print("Data imput is : ", Data)

    FData = list(filter(CheckGreater10,Data))

    print("Data after Filter is :", FData)

if __name__ == "__main__":
    main()