def CheckEven(No):  #No is the parameter that will receive the number.
    if No % 2 == 0:          #Processing
        print("its a even number")
    else:
        print("its odd number ")

def main():
    Value = int(input("Enter a number : "))

    CheckEven(Value)

if __name__ == "__main__":
    main()