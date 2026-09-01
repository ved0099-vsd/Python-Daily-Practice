def main():
    Age = int(input("Enter your Age Please : "))
    Student = input("Are you a Student? (Yes/No): ")

    if(Age <= 24):
        if(Student == "Yes"):
            print("You are eligible for MOvie Discount")
        else:
            print("You are not a student so no discount")
    else:
        print("You are above 24 so no discount")

if __name__ == "__main__":
    main()