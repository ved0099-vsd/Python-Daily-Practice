#Number Checker 🔢

#Take a number.

#Check:

#If it is positive or negative.
#If it is even or odd.

def main():
    No = int(input("Enter a number : "))

    if No > 0:
        print("Positive")
        if No % 2 == 0:
            print("EVEN")
        else:
            print("Odd")
    else:
        print("Negative")
    

if __name__ == "__main__":
    main()