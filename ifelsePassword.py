def main():
    Correct_Password = 1234
    User_Password = int(input("ENter your password :"))

    if (User_Password == Correct_Password):
        print("Login Successfull...")
    else:
        print("Incorrect password")
    
   


if __name__ == "__main__":
    main()