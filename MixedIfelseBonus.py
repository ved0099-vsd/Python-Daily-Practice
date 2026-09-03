#Salary Bonus 💼

#Take:

#Salary
#Years of experience
#Performance rating

#Rules:

#Experience ≥ 5 years AND rating ≥ 8 → 20% bonus.
#Experience ≥ 3 years AND rating ≥ 7 → 10% bonus.
#Otherwise → 5% bonus.

#Calculate bonus amount.

def main():
    Salary = int(input("Enter your salary : "))
    Exp = int(input("Enter your years of experiance  :"))
    Rating = int(input("Enter your rating : "))

    if Exp <=10 and Rating <= 10:
        if Exp >= 5 and Rating >= 8:
                print("Your bonus will be 20percent")
                Bonus = Salary * 0.20
                print("Salary + Bomus will be :",Bonus + Salary)
        
        elif Exp >= 3 and Rating >= 7:
            print("Bonus 10 percent")
            Bonus = Salary * 0.10
            print("Salary + Bonus will be : ",Bonus + Salary)
        
        else:
            Bonus = Salary * 0.5
            print("Salary + Bonus will be ",Bonus + Salary)

    else:
         print("invalid input")






if __name__ == "__main__":
    main()