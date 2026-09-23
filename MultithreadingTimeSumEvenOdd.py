import time

def SumEven(No):
    Sum = 0
    for i in range(2,No,2):
        Sum = Sum + i

    print("Summation of Even is :",Sum)

def SumOdd(No):
    Sum = 0
    for i in range(1,No,2):
        Sum = Sum + i

    print("Summation of Odd is :",Sum)

def main():
    start_time = time.perf_counter()

    SumEven(123456)
    SumOdd(123456)

    end_time = time.perf_counter()

    print(f"time required is : {end_time - start_time:.6f}")

if __name__ == "__main__":
    main()