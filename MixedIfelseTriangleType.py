#Triangle Type 🔺

#Take 3 sides.

#First check whether the triangle is valid.

#If valid:

#All three equal → Equilateral
#Any two equal → Isosceles
#All different → Scalene

def main():
    Side1 = int(input("Enter first side :"))
    Side2 = int(input("Enter second side :"))
    Side3 = int(input("Enter third side :"))

    if Side1 + Side2 > Side3 and Side1 + Side3 > Side2 and Side2 + Side3 > Side1:
        if Side1 == Side2 and Side2 == Side3:
            print("Equilateral Triangle ")

        elif Side1 == Side2 or Side1 == Side3 or Side2 == Side3:
            print("Isosceles triangle")

        else:
            print("Scelene triangle")
    else:
        print("invalid triangle")
        




if __name__ == "__main__":
    main()