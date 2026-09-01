def main():
    Correct_Password = "Ved1234"
    User_password = (input("enter your password : "))

    if(User_password == Correct_Password):
        print("Login Successfull....")
    else:
        print("INcorrect password")

if __name__ == "__main__":
    main()