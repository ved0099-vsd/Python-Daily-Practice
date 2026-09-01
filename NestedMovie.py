def main():
    age = int(input("Enter your age: "))

    if age >= 18:
        ticket = input("Do you have a ticket? (yes/no): ")

        if ticket.lower() == "yes":
            print("Welcome! Enjoy the movie.")
        else:
            print("Please buy a ticket first.")
    else:
        print("Sorry! You are not allowed to enter.")


if __name__ == "__main__":
    main()