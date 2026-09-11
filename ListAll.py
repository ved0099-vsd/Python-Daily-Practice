def main():
    Data = [10,20,30,40,50]

    print(type(Data))   #type() tells you what type of variable Data is.
    print(len(Data))    #len() tells you the number of elements in the list.
    print("-" * 50)

    print(Data[0])     #Python list indexing starts from 0.
    print(Data[1])
    print(Data[2])
    print(Data[3])
    print(Data[4])
    print("-" * 50)

    Data[3] = 69         #Because Python lists are mutable.
                         #Mutable = you can change the values after creating the list.
    print(Data)


if __name__ == "__main__":
    main()