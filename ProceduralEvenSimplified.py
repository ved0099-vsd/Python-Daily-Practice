#The key concept here is:

#Instead of manually returning True or False, directly return the condition.

def CheckEven(No):
    return No % 2 == 0

def main():
    Value = int(input("Enter number : "))

    Ret = CheckEven(Value)

    if(Ret == True):
        print("its Even")
    else:
        print("its odd")

if __name__ == "__main__":
    main()