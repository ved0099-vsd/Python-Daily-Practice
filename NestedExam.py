def main():
    Marks = int(input("Enter MArks : "))
    Attendance = int(input("Enter your Attendance in Number : "))

    if Marks >= 60:
        if Attendance >= 40:
            print("Yes you are passed")
        else:
            print("Not enough attendance")

    else:
        print("Low marks failed")

if __name__ == "__main__":

    main()