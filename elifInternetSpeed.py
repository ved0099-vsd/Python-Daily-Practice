def main():
    Internet_Speed = float(input("enter INternet Speed : "))

    if(Internet_Speed <= 10):
        print("No Internet")

    elif(Internet_Speed <= 50):
        print("Low connectivity")

    elif(Internet_Speed <= 80):
        print("Good conectivity")

    elif(Internet_Speed <= 150):
        print("Best connectivity")

    elif(Internet_Speed > 150):
        print("Full Speed connectivity")

    else:
        print("Enter Something bitch")
    

if __name__ == "__main__":
    main()
