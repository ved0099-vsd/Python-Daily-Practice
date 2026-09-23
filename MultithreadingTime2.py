import time
import threading

def SumEven(No):
    Sum = 0
    for i in range(2,No,2):
        Sum = Sum + i

    print(f"summation of even is {Sum} ")

def SumOdd(No):
    Sum = 0
    for i in range(1,No,2):
        Sum = Sum + i

    print(f"summation of odd is {Sum} ")

def main():
    start_time = time.perf_counter()

    t1 = threading.Thread(target=SumEven, args = (23456,))
    t2 = threading.Thread(target=SumOdd, args=(1234567,))

    t1.start()
    t2.start()

    end_time = time.perf_counter()

    print(f"time required is {end_time - start_time:.3f}")

if __name__ == "__main__":
    main()