def main():
    print("Enter your attendence : ")
    Attendence = int(input())

    if(Attendence >= 75):
        print("yes you are eligible for exam")
    else:
        print("No you aer not eligible for exam")

if __name__ == "__main__":
    main()