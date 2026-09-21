def CheckRange(No):
    return No >= 10 and No <=50

def main():

    Data = [12,34,76,35,23,76,78,23,55,66,12,21,22,3,44,55]

    print("Input Data is : ",Data)

    FData = list(filter(CheckRange,Data))

    print("Data after filter is : ", FData)

if __name__ == "__main__":
    main()