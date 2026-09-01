def main():
    Username = input("Enter Username : ")
    Password = int(input("Enter Password : "))

    if(Username == "admin"):
        if(Password == 1234):
            print("Login Successfull.....")
        else:
            print("Incorrect Password ")
    else:
        print("Incorrect Username ")

if __name__ == "__main__":
    main()