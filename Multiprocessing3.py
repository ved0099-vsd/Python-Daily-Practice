import os
import multiprocessing
import time

def SumEven(No):
    print(f"PID of SumEven : {os.getpid()} PPID of SumEVen :{os.getppid()}")

    Sum = 0

    for i in range(2,No,2):
        Sum = Sum + i

    print("Summation of even : ",Sum)

def SumOdd(No):
    print(f"PID of SumOdd : {os.getpid()} PPID of SumOdd :{os.getppid()}")

    Sum = 0

    for i in range(1,No,2):
        Sum = Sum + i

    print("Summation of odd : ",Sum)

def main():
    print(f"PID of Main : {os.getpid()} PPID of main : {os.getppid()}")

    start_time = time.perf_counter()

    t1 = multiprocessing.Process(target=SumEven, args=(100000,))
    t2 = multiprocessing.Process(target=SumOdd, args = (100000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"Time required is : {end_time - start_time:.5f}")

if __name__ == "__main__":
    main()