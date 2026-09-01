def main():
    Username = input("Enter your Username :")
    Password = int(input("Enter your Password : "))
    Status = input("account active or not (Active/Inactive) : ")

    if Username == "Ved1234":
        if Password == 12345:
            if Status == "Active":
                print("Yes Login Successfully Netflix and Chill!!!!")
            else:
                print("Your Account is not Active")
        else:
            print("Incorrect PAssword")
    else:
        print("INvalid Username ")

if __name__ == "__main__":
    main()