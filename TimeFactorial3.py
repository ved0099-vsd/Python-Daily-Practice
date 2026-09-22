import time

def Factorial(No):
    Fact = 1
    for i in range(1,No + 1):
        Fact = Fact * i
    return Fact

def main():
    Value = int(input("Enter a number : "))

    start_time = time.perf_counter() #perf_counter() is designed for measuring short durations / execution time, so it's a better choice for this program.

    Ret = Factorial(Value)

    end_time = time.perf_counter()  # End time

    print(f"Factorial of {Value} is {Ret}")
    print(f"Time required is {end_time - start_time:.5f} Seconds") # :.5f
#   it means display the result with 5 digits after the decimal point.

if __name__ == "__main__":
    main()