def Division(No):
    return No % 5 == 0

def main():
    Data = [21,30,45,67,55,98,100]

    print("Data from Imput is : ",Data)

    FData = list(filter(Division,Data))

    print("Data after Filter is : ",Data)

if __name__ == "__main__":
    main()