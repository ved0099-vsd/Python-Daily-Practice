import time

def Factorial(No):
    Fact = 1
    for i in range(1,No + 1):
        Fact = Fact * i
    return Fact

def main():
    Value = int(input("enter a number : "))

    start_time = time.time()  # Start time

    Ret = Factorial(Value)

    end_time = time.time()   # End time
  
    print(f"Factorial of {Value} is {Ret}")

    print(f"time required for finding out factorial is {end_time - start_time} Seconds")
 

if __name__ == "__main__":
    main()