def main():
    Attendance = int(input("Enter your Attendance in days : "))
    Ticket = input("Have you taken Hall Ticket ? (YES/NO) :")
    Fees = input("Have you paid all your Fees? (YES/NO) : ")

    if(Attendance >= 120):
        if(Ticket == "YES"):
            if Fees == "YES":
                print("YEs you can take the exam")
            else:
                print("Fees not Paid so no exam")
        else:
            print("Hall ticket not taken so no exam")
    else:
        print("Low Attendance so no exam")

if __name__ == "__main__":
    main()