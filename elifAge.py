def main():
    Age = int(input("Enter your Age : "))

    if(Age >= 60):
        print("You are senior person")
    elif(Age >= 35):
        print("You are a Adult")
    elif(Age >= 18):
        print("you are a Young person")
    elif(Age > 12):
        print("You are a Teenager")
    else:
        print("You are a child")

if __name__ == "__main__":
    main()