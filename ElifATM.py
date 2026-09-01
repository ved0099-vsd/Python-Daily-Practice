def main():
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Checking Balance")

    elif choice == 2:
        print("Withdraw")

    elif choice == 3:
        print("Deposit")

    elif choice == 4:
        print("Exit")
        
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()