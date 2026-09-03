#Job Eligibility 💼

#Take:
#Age
#Qualification (graduate / postgraduate)
#Experience in years

#Rules:
#A candidate is eligible if:

#Age is 21 or above
#AND qualification is graduate or postgraduate
#AND experience is 2 or more years

#Otherwise, print "Not eligible".

#If eligible, print "Eligible for the job".

def main():
    Age = int(input("Enter your age : "))
    Qualification = input("Enter your qualification (graduate/postgraduate) :  ")
    Exp = int(input("Enter your Experiance in years : "))

    if Age >= 21 and Qualification is "graduate" or "postgraduate" and Exp >= 2 :
        print("Eligible")
    else:
        print("Not eligible")

if __name__ == "__main__":
    main()