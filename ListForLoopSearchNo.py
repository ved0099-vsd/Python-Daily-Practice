def main():
    Data = [10,20,30,40,50]
    Value = int(input("Enter a number : "))

    Found = False

    for i in Data:
        if i == Value:
            Found = True

    if Found == True:
        print("Number is present")
    else:
        print("Number is not present")

if __name__ == "__main__":
    main()