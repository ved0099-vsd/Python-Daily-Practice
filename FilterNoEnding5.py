def Ending5(No):
    return No % 10 == 5

def main():
    Data = [23,34,65,87,50,40,53,35,55,25]

    print("Data is : ",Data)

    FData = list(filter(Ending5,Data))

    print("Data after filter is : ",FData)

if __name__ == "__main__":
    main()
    