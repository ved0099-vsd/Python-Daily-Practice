def main():
    Age = int(input("Enter your Age : "))

    if(Age <= 8):
        print("Free entry")
    elif(Age >= 15):
        print("150 Rupees")
    else:
        print("Enter age ")

if __name__ == "__main__":
    main()