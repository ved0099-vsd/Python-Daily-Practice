# 2 + 4 + 6 + 8 = 20

def SumEven(No):
    Sum = 0

    for i in range(2,No,2):
        Sum = Sum + i      #Adds each even number to Sum.

    print("Summation of even :",Sum)

# 1 + 3 + 5 + 7 + 9 = 25

def SumOdd(No):
    Sum = 0

    for i in range(1,No,2):
        Sum = Sum + i

    print("Summation of odd numbers is :",Sum)

def main():
    SumEven(19999)
    SumOdd(199999)

if __name__ == "__main__":
    main()