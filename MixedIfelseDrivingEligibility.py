#Driving Eligibility 🏍️

#Take:

#Age
#Licence (yes/no)

#Rules:

#If age is 18 or above, check the licence.

#Age ≥ 18 + licence yes → "You can drive"
#Age ≥ 18 + licence no → "Get a licence first"
#Age < 18 → "You are underage"

def main():
    Age = int(input("Enter your Age : "))
    License = input("Do you have license ? (yes/no)")

    if Age >= 18:
        if License == "yes":
            print("You can drive")
        else:
            print("GO get a license")
    else:
        print("you are underage")
    


if __name__ == "__main__":
    main()