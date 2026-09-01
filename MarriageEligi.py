Age = (int(input("Enter your Age : ")))
Gender = input("Enter your Gender (M/F): ")

if Gender.upper() == "M":
    if(Age >= 21):
        print("Yes you are eligible for marriage : ")
    else:
        print("You are not eligible ")
elif Gender.upper() == "F":
    if(Age >= 18):
        print("Yes you are eligible")
    else:
        print("Not eligible")

