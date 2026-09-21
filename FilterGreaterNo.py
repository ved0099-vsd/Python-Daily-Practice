def Greater50(No):
    return No >= 50

def main():
    Data = [65,89,23,56,96,57,23,90]

    print("Data is : ",Data)

    FData = list(filter(Greater50,Data))

    print("Data after filter is : ",FData)

if __name__ == "__main__":
    main()