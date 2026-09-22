import time

def Factorial(No):
    Fact = 1
    for i in range(1,No + 1):
        Fact = Fact * i
    return Fact

def main():
    Value = int(input("Enter a number : "))

    start_time = time.perf_counter() #Start time

    Ret = Factorial(Value)

    end_time = time.perf_counter()  # End time

    print(f"Factorial of {Value} is {Ret}")
    print(f"Time required is {end_time - start_time: .5f} Seconds")


if __name__ == "__main__":
    main()