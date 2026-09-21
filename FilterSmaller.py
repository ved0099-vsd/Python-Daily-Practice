def Smaller50(No):
    return No <= 50

def main():
    Data = [12,5,654,75,34,75,32,12,98,8765,2,5]

    print("input Data is : ", Data)

    FData = list(filter(Smaller50,Data))

    print("Data after Filter is : ", FData)

if __name__ == "__main__":
    main()