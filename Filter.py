def CheckEven(No):
    return No % 2 == 0

def main():
    Data = [13,12,45,64,24,998,33,56,78,91]

    print("Input Data is : ",Data)

    FData = list(filter(CheckEven,Data))

    print("Data after filter : ", FData)

if __name__ == "__main__":
    main()