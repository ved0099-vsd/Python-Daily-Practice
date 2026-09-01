def main():
    Weight = int(input("Enter your Weight : "))

    if(Weight <= 30):
        print("Under weight", Weight)

    elif(Weight <= 50):
        print("Ok weight", Weight)

    elif(Weight >= 85):
        print("Overweight", Weight)

    elif(Weight <= 84):
        print("Slightly over weight", Weight)

    else:
        print("OBESE")

if __name__ == "__main__":
    main()