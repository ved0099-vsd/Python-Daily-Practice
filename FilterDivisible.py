def Divisible3(No):
    return No % 3 == 0

def main():
    Data = [12,23,54,65,98,66,43]

    print("Data is : ",Data)

    FData = list(filter(Divisible3,Data))

    print("Data after filter is : ", FData)

if __name__ == "__main__":
    main()