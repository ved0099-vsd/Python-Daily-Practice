#Driving Test 🏍️

#Take:

#Age
#Learner licence (yes/no)
#Test result (pass/fail)

#Rules:

#Age must be ≥ 18
#Must have learner licence
#Must pass the test

#Only when all three conditions are satisfied:

#"Driving licence approved"

def main():
    Age = int(input("Enter your AGe : "))
    License = input("do you have a  learning license (yes/no) : ")
    Test = input("test result (pass/fail) : ")

    if Age >= 18:
        if License == "yes":            
            if Test == "pass":
                print("Driving license approved")
            else:
                print("drvinvg license rejected")
        else:
            print("get learners license first")
    else:
        print("You are a minor")

if __name__ == "__main__":
    main()