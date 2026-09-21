def GreaterEven(No):
    return No >= 25 and No % 2 == 0

def main():
    Data = [10,12,34,54,66,75,87,40,30,70]

    print("Data is ",Data)

    FData = (list(filter(GreaterEven,Data)))

    print("Data after filter is : ", FData)

if __name__ == "__main__":
    main()