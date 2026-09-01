#Student Result 🎓
#Take:
#Marks
#Attendance
#Assignment status (yes/no)

#Rules:
#Attendance must be 75% or more.
#Marks must be 40 or more.
#Assignment must be submitted.

def main():
    Marks = int(input("Enter Marks : "))
    Attendance = int(input("Enter Attendance in days : "))
    Assignment = input("Have you completed all assignmets : (yes/no)")

    if Marks >= 40:
        if Attendance >= 75:
            if Assignment == "yes":
                print("Yes you are passed")
            else:
                print("Assignments not completed")
        else:
            print("Attendance is low")
    else:
        print("Marks are below 40")

if __name__ == "__main__":
    main()