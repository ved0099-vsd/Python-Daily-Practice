def main():

    Salary = int(input("Enter salary :"))

    if(Salary <= 25000):
        print("Fresher")

    elif(Salary <= 50000):
        print("Junior Level")

    elif(Salary <= 70000):
        print("Senior Level")  

    elif(Salary >= 71000):
        print("Super Senior Level")  

if __name__ == "__main__":
    main()