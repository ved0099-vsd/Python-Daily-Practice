def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter a number : "))

    Ret = CheckEven(Value)

    if(Ret == True):
        print("its even")
    else:
        print("its odd")

if __name__ == "__main__":
    main()
