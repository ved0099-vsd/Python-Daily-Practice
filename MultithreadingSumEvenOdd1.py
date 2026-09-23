def SumEven(No):
    Sum = 0
    for i in range(2,No,2):
        Sum = Sum + i

    print("Summation of Even numbers is :",Sum)

def SumOdd(No):
    Sum = 0
    for i in range(1,No,2):
        Sum = Sum + i

    print("Summation of Odd numbers is : ",Sum)

def main():
    SumEven(68)
    SumOdd(69)


if __name__ == "__main__":
    main()