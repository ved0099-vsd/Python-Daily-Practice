CheckEven = lambda No : (No % 2 == 0)

def main():
    Value = int(input("Enter number : "))

    Ret = CheckEven(Value)    #Ret = (Value % 2 == 0)

    if Ret == True:
        print("its even")
    else:
        print("its odd")

if __name__ == "__main__":
    main()