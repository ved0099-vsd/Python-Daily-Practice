def main():
    Units = int(input("Enter electricity units : "))

    if(Units < 100):
        print("Bill will be 5 rupees per unit thats : ",Units * 5)
    elif(Units < 200):
        print("Bill will be 7 rupees per unit thats : ", Units * 7)
    else:
        print("Bill will be 10 rupees per unit thats : ", Units * 10)


if __name__ == "__main__":
    main()