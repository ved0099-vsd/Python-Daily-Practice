def main():
    print("Enter a number : ")
    No = int(input())

    if(No > 0):
        print("No. is positive",No)

    elif(No == 0):
        print("Number is 0")

    else:
        print("No. is Negative",No)

if __name__ == "__main__":
    main()