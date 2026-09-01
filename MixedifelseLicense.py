#Driving Eligibility 🚗
#Take:
#Age
#Learner licence (yes/no)
#Driving test result (pass/fail)

#Rules:
#Age must be 18+.
#Learner licence must be available.
#Driving test must be passed.

def main():
    Age = int(input("Enter your Age : "))
    Learner_license = input("Do you have a Learners license : (yes/no)")
    Driving_test_result = input("Have you passed the Driving test ? (yes/no) : ")

    if Age >= 18:
        if Learner_license == "yes":
            if Driving_test_result == "yes":
                print("here's your Driving License")
            else:
                print("You have not passed the driving ")
        else:
            print("you dont have a learners license")
    else:
        print("You are a minor")

if __name__ == "__main__":
    main()