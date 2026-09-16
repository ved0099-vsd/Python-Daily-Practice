#Check if number is NOT present

def main():
    Data = (11,12,13,14,15,16)
    Num = int(input("Enter a number : "))

    if Num not in Data:                     #not in.
        print("Number is not in Data")
    else:
        print("Number is present in data") 

        

if __name__ == "__main__":
    main()