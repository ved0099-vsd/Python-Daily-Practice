def main():
    num = int(input("Enter a number : "))

    Data = (1,2,3,4,5,67,8,9,0,12,23,45,69,54,24,65)

    if num in Data:
        print("that number is present ")
    else:
        print("number is absent")

if __name__ == "__main__":
    main()