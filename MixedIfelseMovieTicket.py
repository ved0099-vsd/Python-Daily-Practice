#Movie Ticket 🎬

#Take:
#Age
#Student status
#Day

#Rules:

#Below 5 → Free.
#5–17 → ₹100.
#18–59 → ₹200.
#60+ → ₹120.
#Students get ₹50 discount, except on Sunday.
#Calculate the final ticket price.

def main():
    Age = int(input("Enter your Age : "))
    Student_status = input("Are you a Student ? (yes/no) : ")
    Day = input("ENter Your movie DAY : ")

    if Age <= 5:
        print("Free entry")
    elif Age <= 17:
        if Student_status == "yes":
            if Day == "sunday":
                print("No discount pay 100 rupees")
            else:
                print("50 rupees discount for students")
        else:
            print("no discount for non students")

    elif Age <= 59:
        if Student_status == "yes":
            if Day == "sunday":
                print("No discount pay 200 rupees")
            else:
                print("50 rupees discount for students")
        else:
            print("no discount for non students")

    else:
        print("ticket 120")

        



        




        


                

if __name__ == "__main__":
    main()