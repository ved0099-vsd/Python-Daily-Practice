#Employee Bonus 💼

#Take:

#Salary
#Years of experience

#Rules:

#Experience ≥ 5 years → 20% bonus
#Experience 2–4 years → 10% bonus
#Experience < 2 years → 5% bonus

#But if salary is below ₹20,000, give no bonus.

#Print the bonus amount and final salary.

def main():

    Salary = int(input("Enter your salary : "))
    Exp = int(input("Enter your Years of Experience"))

    if Exp >= 5:
        Bonus = Salary * 0.20
        Bonus = Salary + Bonus
        print("Your Bonus will be ",Bonus)
    elif Exp >= 2:
        Bonus = Salary * 0.10
        Bonus = Salary + Bonus
        print("Your Bonus will be ",Bonus)
    else:
        Bonus = Salary * 0.5
        Bonus = Salary + Bonus
        print("Bonus = ",Bonus)


          
if __name__ == "__main__":
    main()