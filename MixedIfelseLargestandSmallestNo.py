#Largest and Smallest

#Take three numbers.

#Print:

#Largest
#Smallest
#Whether any two numbers are equal.

def main():
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a number : "))
    num3 = int(input("Enter a number : "))

#largest
    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

#smallest

    if num1 <= num2 and num1 <= num3:
        smallest = num1
    elif num2 <= num1 and num2 <= num3:
        smallest = num2
    else:
        smallest = num3

#equal no's

    if num1 == num2 or num1 == num3 or num2 == num3:
        print("Two nos are equal")
    else:
        print("all nos are diff")

    print("largest no is ",largest)
    print("smallest no. is ",smallest)




if __name__ == "__main__":
    main()
