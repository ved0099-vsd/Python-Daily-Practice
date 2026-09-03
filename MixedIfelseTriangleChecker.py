#Triangle Checker 🔺

#Take three sides.

#First check whether the three sides can form a triangle.

#If they can, determine whether it is:

#Equilateral
#Isosceles
#Scalene


def main():
    side1 = int(input("enter first side : "))
    side2 = int(input("enter second side : "))
    side3 = int(input("enter third side : "))

    if side1 + side2 > side3 and side1 + side3 > side2 and side2 +side3 > side1:

        if side1 == side2 and side2 == side3:
            print("Equilateral Triangle")

        elif side1 == side2 or side1 == side3 or side2 == side3:
            print("Isosceles triangle")

        else:
            print("Scalene Triangle")
    else:
        print("Invalid Triangle")

if __name__ == "__main__":
    main()