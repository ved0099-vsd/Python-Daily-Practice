import time
import multiprocessing

def SumEven(No):
    Sum = 0
    for i in range(2,No,2):
        Sum = Sum + i
    print(f"Summation of even is {Sum}")

def SumOdd(No):
    Sum = 0
    for i in range(1,No,2):
        Sum = Sum + i
    print(f"Summation of even is {Sum}")

def main():
    start_time = time.perf_counter()

    t1 = multiprocessing.Process(target=SumEven, args = (100000000,))
    t2 = multiprocessing.Process(target=SumOdd, args = (1000000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.perf_counter()

    print(f"required time is { end_time - start_time:.5f}")



if __name__ == "__main__":
    main()
