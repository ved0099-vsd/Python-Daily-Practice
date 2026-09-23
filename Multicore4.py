import time

def SumCube(No):
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + (i ** 3)
    return Sum

def main():
    Data = [100000000, 200000000, 300000000, 4000000000, 50000000000]
    result =[]

    start_time = time.perf_counter()

    for Value in Data:
        Ret = SumCube(Value)
        result.append(Ret)

    end_time = time.perf_counter()

    print("Result is :")
    print(result)

    print(f"time required is : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()