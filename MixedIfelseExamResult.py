#exam Result 📝

#Take:

#Marks
#Attendance

#Rules:

#Attendance must be 75 or above
#Marks must be 40 or above

def main():
    Marks = int(input("Enter your Marks : "))
    Attendance = int(input("Enter your Attendance between 0 to 100 : "))

    if Marks >= 40 and Attendance >= 75:  #and
        print("You passed")
    else:
        print("You failed")



if __name__ == "__main__":
    main()