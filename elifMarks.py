def main():
    Marks = int(input("enter your Marks : "))

    if(Marks >= 90):
        print("A+ grade")

    elif(Marks >= 75 ):
        print("A grade")

    elif(Marks >= 60):
        print("B+ grade")

    elif(Marks >= 50):
        print("B grade")

    elif(Marks >= 45):
        print("C grade")

    elif(Marks >= 35):
        print("D grade")

    else:
        print("Fail")
    



if __name__ == "__main__":
    main()