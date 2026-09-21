def CheckEven(No):
    if No % 2 == 0:
        return True  #The function does not print anything. It only returns the answer:
    else:
        return False

def main():
    Value = int(input("Enter number : "))

    Ret = CheckEven(Value)
    #Input → CheckEven() → True/False → Ret → if/else → Output
    if Ret == True:
        print("its even")
    else:
        print("its odd")

if __name__ == "__main__":
    main()