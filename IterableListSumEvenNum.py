def SumEven(Data):
    Sum = 0

    for no in Data:
        if no % 2 == 0:
            Sum = Sum + no

    return Sum

def main():
    Data = [12,10,33,67,99,68]

    Ret = SumEven(Data)

    print("Addition of even numbers is : ", Ret)

if __name__ == "__main__":
    main()